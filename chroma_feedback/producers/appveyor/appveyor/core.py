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
		program.add_argument('--appveyor-host', default = 'https://ci.appveyor.com')
		program.add_argument('--appveyor-slug', action = 'append')
		program.add_argument('--appveyor-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	if ARGS.get('appveyor_slug'):
		for slug in ARGS.get('appveyor_slug'):
			result.extend(fetch(ARGS.get('appveyor_host'), slug, ARGS.get('appveyor_token')))
	else:
		result.extend(fetch(ARGS.get('appveyor_host'), None, ARGS.get('appveyor_token')))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/api/projects/' + slug, headers = request.create_bearer_auth_headers(token))
	elif host and token:
		response = request.get(host + '/api/projects', headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)
		data_account = helper.deep_get(data, [ 'project', 'accountName' ])
		data_project = helper.deep_get(data, [ 'project', 'slug' ])
		data_status = helper.deep_get(data, [ 'build', 'status' ])

		if data_account and data_project and data_status:
			result.append(normalize_data(data_account + '/' + data_project, data_status))

		data_builds = helper.deep_get(helper.get_first(data), [ 'builds' ])

		if data_builds:
			for project in data:
				data_account = project.get('accountName')
				data_project = project.get('slug')
				data_build = helper.get_first(project.get('builds'))
				data_status = helper.deep_get(data_build, [ 'status' ])

				if data_account and data_project and data_status:
					result.append(normalize_data(data_account + '/' + data_project, data_status))
	return result
