from argparse import ArgumentParser
from typing import Any, List

from chroma_feedback import helper, request
from chroma_feedback.typing import Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--netlify-host', default = 'https://api.netlify.com')
		program.add_argument('--netlify-slug', action = 'append')
		program.add_argument('--netlify-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	if ARGS.netlify_slug:
		for slug in ARGS.netlify_slug:
			result.extend(fetch(ARGS.netlify_host, slug, ARGS.netlify_token))
	else:
		result.extend(fetch(ARGS.netlify_host, None, ARGS.netlify_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []

	if host and slug and token:
		result.extend(fetch_build(host, slug, token))
	elif host and token:
		sites = fetch_sites(host, token)

		for site in sites:
			result.extend(fetch_build(host, site['id'], token))
	return result


def fetch_build(host : str, slug : str, token : str) -> List[Producer]:
	result : List[Producer] = []
	response = None

	if host and slug and token:
		response = request.get(host + '/api/v1/sites/' + slug + '/deploys', headers = request.create_bearer_auth_headers(token))

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)
		build = helper.get_first(data)

		if build and 'name' in build and 'admin_url' in build and 'state' in build:
			result.append(normalize_data(build['name'], build['admin_url'], build['state']))
	return result


def fetch_sites(host : str, token : str) -> List[Any]:
	result = []
	response = None

	if host and token:
		response = request.get(host + '/api/v1/sites', headers = request.create_bearer_auth_headers(token))

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		for site in data:
			if 'id' in site:
				result.append(site)
	return result
