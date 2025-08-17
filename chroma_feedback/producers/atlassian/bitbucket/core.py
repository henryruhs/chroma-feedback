from argparse import ArgumentParser
from typing import Any, List, Optional, cast

from chroma_feedback import helper, request
from chroma_feedback.types import Producer
from .normalize import normalize_data
from .types import Args

ARGS : Optional[Args] = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--atlassian-bitbucket-host', default = 'https://api.bitbucket.org')
		program.add_argument('--atlassian-bitbucket-slug', action = 'append', required = True)
		program.add_argument('--atlassian-bitbucket-username', required = True)
		program.add_argument('--atlassian-bitbucket-password', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []
	auth = fetch_auth(ARGS.get('atlassian_bitbucket_host'), ARGS.get('atlassian_bitbucket_username'), ARGS.get('atlassian_bitbucket_password'))

	if 'access_token' in auth:
		for slug in ARGS.get('atlassian_bitbucket_slug'):
			result.extend(fetch(ARGS.get('atlassian_bitbucket_host'), slug, auth['access_token']))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/2.0/repositories/' + slug + '/pipelines/', headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'values' in data:
			data_build = helper.get_last(data['values'])

			data_slug = helper.deep_get(data_build, [ 'repository', 'full_name' ])
			data_status = helper.deep_get(data_build, [ 'state', 'name' ])
			data_result = helper.deep_get(data_build, [ 'state', 'result', 'name' ])

			if data_slug and data_status and data_result:
				result.append(normalize_data(data_slug, data_status, data_result))
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
		access_token = data.get('access_token')

		if access_token:
			result['access_token'] = access_token
	return result
