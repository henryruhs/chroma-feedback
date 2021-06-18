from typing import List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from chroma_feedback.typing import ProducerModel
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--appveyor-host', default = 'https://ci.appveyor.com')
		program.add_argument('--appveyor-slug', action = 'append')
		program.add_argument('--appveyor-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[ProducerModel]:
	result = []

	if ARGS.appveyor_slug:
		for slug in ARGS.appveyor_slug:
			result.extend(fetch(ARGS.appveyor_host, slug, None))
	else:
		result.extend(fetch(ARGS.appveyor_host, None, ARGS.appveyor_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[ProducerModel]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/api/projects/' + slug, headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Bearer ' + token
		})
	elif host and token:
		response = request.get(host + '/api/projects', headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'project' in data and 'accountName' in data['project'] and 'build' in data and 'status' in data['build']:
			result.append(normalize_data(data['project']['accountName'] + '/' + data['project']['slug'], data['build']['status']))
		if 'builds' in helper.get_first(data):
			for project in data:
				build = helper.get_first(project['builds'])

				if project and 'accountName' in project and 'slug' in project and build and 'status' in build:
					result.append(normalize_data(project['accountName'] + '/' + project['slug'], build['status']))
	return result
