from argparse import ArgumentParser
from typing import List, Optional, cast

from chroma_feedback import helper, request
from chroma_feedback.types import Producer
from .normalize import normalize_data
from .types import Args

ARGS : Optional[Args] = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--jetbrains-teamcity-host', default = 'https://teamcity.jetbrains.com')
		program.add_argument('--jetbrains-teamcity-slug', action = 'append')
		program.add_argument('--jetbrains-teamcity-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	if ARGS.get('jetbrains_teamcity_slug'):
		for slug in ARGS.get('jetbrains_teamcity_slug'):
			result.extend(fetch(ARGS.get('jetbrains_teamcity_host'), slug, ARGS.get('jetbrains_teamcity_token')))
	else:
		result.extend(fetch(ARGS.get('jetbrains_teamcity_host'), None, ARGS.get('jetbrains_teamcity_token')))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/app/rest/buildTypes/?fields=buildType(builds($locator(running:any),build(webUrl,status,running,buildType(projectName,paused))))&locator=affectedProject:(id:' + slug + ')', headers = request.create_bearer_auth_headers(token))
	elif host and token:
		response = request.get(host + '/app/rest/buildTypes/?fields=buildType(builds($locator(running:any),build(webUrl,status,running,buildType(projectName,paused))))', headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'buildType' in data:
			for project in data['buildType']:
				data_builds = helper.deep_get(project, [ 'builds', 'build' ])

				if data_builds:
					build = helper.get_first(data_builds)
					data_project = helper.deep_get(build, [ 'buildType', 'projectName' ])
					data_url = helper.deep_get(build, [ 'webUrl' ])
					data_status = helper.deep_get(build, [ 'status' ])
					data_paused = helper.deep_get(build, [ 'buildType', 'paused' ])
					data_running = helper.deep_get(build, [ 'running' ])

					if build and data_project and data_url and data_status and data_paused and data_running:
						result.append(normalize_data(data_project, data_url, data_status, data_paused, data_running))
	return result
