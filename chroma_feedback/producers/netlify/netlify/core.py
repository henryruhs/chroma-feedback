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
		program.add_argument('--netlify-host', default = 'https://api.netlify.com')
		program.add_argument('--netlify-slug', action = 'append')
		program.add_argument('--netlify-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	if ARGS.get('netlify_slug'):
		for slug in ARGS.get('netlify_slug'):
			result.extend(fetch(ARGS.get('netlify_host'), slug, ARGS.get('netlify_token')))
	else:
		site_ids = fetch_site_ids(ARGS.get('netlify_host'), ARGS.get('netlify_token'))

		if site_ids:
			for site_id in site_ids:
				result.extend(fetch(ARGS.get('netlify_host'), site_id, ARGS.get('netlify_token')))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result : List[Producer] = []
	response = None

	if host and slug and token:
		response = request.get(host + '/api/v1/sites/' + slug + '/deploys', headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)
		build = helper.get_first(data)

		if build and 'name' in build and 'admin_url' in build and 'state' in build:
			result.append(normalize_data(build['name'], build['admin_url'], build['state']))
	return result


def fetch_site_ids(host : str, token : str) -> List[str]:
	result = []
	response = None

	if host and token:
		response = request.get(host + '/api/v1/sites', headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		for site in data:
			if 'id' in site:
				result.append(site['id'])
	return result
