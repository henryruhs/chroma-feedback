from argparse import ArgumentParser
from typing import Dict, List

from chroma_feedback import helper, request
from chroma_feedback.typing import Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--heroku-host', default = 'https://api.heroku.com')
		program.add_argument('--heroku-slug', action = 'append')
		program.add_argument('--heroku-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	if ARGS.heroku_slug:
		for slug in ARGS.heroku_slug:
			result.extend(fetch(ARGS.heroku_host, slug, ARGS.heroku_token))
	else:
		for slug in fetch_slugs(ARGS.heroku_host, ARGS.heroku_token):
			result.extend(fetch(ARGS.heroku_host, slug, ARGS.heroku_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/apps/' + slug + '/releases', headers = _create_headers(token))

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)
		build = helper.get_last(data)

		if 'app' in build and 'name' in build['app'] and 'status' in build:
			result.append(normalize_data(build['app']['name'], build['status']))
	return result


def fetch_slugs(host : str, token : str) -> List[str]:
	result = []
	response = None

	if host and token:
		response = request.get(host + '/apps', headers = _create_headers(token))

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		for application in data:
			if 'name' in application:
				result.append(application['name'])
	return result


def _create_headers(token : str) -> Dict[str, str]:
	return\
	{
		'Accept': 'application/vnd.heroku+json;version=3',
		'Authorization': 'Bearer ' + token
	}