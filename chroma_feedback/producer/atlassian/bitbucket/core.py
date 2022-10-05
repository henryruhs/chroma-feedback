from argparse import ArgumentParser
from typing import Any, List

from chroma_feedback import helper, request
from chroma_feedback.typing import Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--atlassian-bitbucket-host', default = 'https://api.bitbucket.org')
		program.add_argument('--atlassian-bitbucket-slug', action = 'append', required = True)
		program.add_argument('--atlassian-bitbucket-username', required = True)
		program.add_argument('--atlassian-bitbucket-password', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []
	auth = fetch_auth(ARGS.atlassian_bitbucket_host, ARGS.atlassian_bitbucket_username, ARGS.atlassian_bitbucket_password)

	if 'access_token' in auth:
		for slug in ARGS.atlassian_bitbucket_slug:
			result.extend(fetch(ARGS.atlassian_bitbucket_host, slug, auth['access_token']))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/2.0/repositories/' + slug + '/pipelines/', headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'values' in data:
			build = helper.get_last(data['values'])

			if build and 'repository' in build and 'full_name' in build['repository'] and 'state' in build and 'name' in build['state']:
				if 'result' in build['state'] and 'name' in build['state']['result']:
					result.append(normalize_data(build['repository']['full_name'], build['state']['name'], build['state']['result']['name']))
				else:
					result.append(normalize_data(build['repository']['full_name'], build['state']['name'], None))
	return result


def fetch_auth(host : str, username : str, password : str) -> Any:
	result = {}
	response = None

	if host and username and password:
		response = request.post(host.replace('api.', '') + '/site/oauth2/access_token',
		{
			'grant_type': 'client_credentials'
		}, headers = request.create_basic_auth_headers(username, password))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'access_token' in data:
			result['access_token'] = data['access_token']
	return result
