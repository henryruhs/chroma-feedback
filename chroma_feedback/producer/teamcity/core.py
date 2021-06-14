from typing import List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from chroma_feedback.typing import ProducerModel
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--teamcity-host', default = 'https://teamcity.jetbrains.com')
		program.add_argument('--teamcity-slug', action = 'append')
		program.add_argument('--teamcity-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[ProducerModel]:
	result = []

	if ARGS.teamcity_slug:
		for slug in ARGS.teamcity_slug:
			result.extend(fetch(ARGS.teamcity_host, slug, ARGS.teamcity_token))
	else:
		result.extend(fetch(ARGS.teamcity_host, None, ARGS.teamcity_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[ProducerModel]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/app/rest/buildTypes/?fields=buildType(builds($locator(running:any),build(running,status,buildType(projectName,paused))))&locator=affectedProject:(id:' + slug + ')', headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Bearer ' + token
		})
	elif host and token:
		response = request.get(host + '/app/rest/buildTypes/?fields=buildType(builds($locator(running:any),build(running,status,buildType(projectName,paused))))', headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'buildType' in data:
			for project in data['buildType']:
				if 'builds' in project and 'build' in project['builds']:
					build = helper.get_first(project['builds']['build'])

					if build and 'buildType' in build and 'projectName' in build['buildType'] and 'paused' in build['buildType'] and 'status' in build and 'running' in build:
						result.append(normalize_data(build['buildType']['projectName'], build['buildType']['paused'], build['status'], build['running']))
	return result
