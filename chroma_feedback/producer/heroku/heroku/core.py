from argparse import ArgumentParser
from typing import List, Optional, cast

from chroma_feedback import helper, request
from chroma_feedback.types import Headers, Producer
from .normalize import normalize_data
from .types import Args

ARGS : Optional[Args] = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--heroku-host', default = 'https://api.heroku.com')
		program.add_argument('--heroku-slug', action = 'append')
		program.add_argument('--heroku-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	if ARGS.get('heroku_slug'):
		for slug in ARGS.get('heroku_slug'):
			result.extend(fetch(ARGS.get('heroku_host'), slug, ARGS.get('heroku_token')))
	else:
		application_ids = fetch_application_ids(ARGS.get('heroku_host'), ARGS.get('heroku_token'))

		if application_ids:
			for application_id in application_ids:
				result.extend(fetch(ARGS.get('heroku_host'), application_id, ARGS.get('heroku_token')))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/apps/' + slug + '/releases', headers = create_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)
		build = helper.get_last(data)

		if build and 'app' in build and 'name' in build['app'] and 'status' in build:
			result.append(normalize_data(build['app']['name'], build['status']))
	return result


def fetch_application_ids(host : str, token : str) -> List[str]:
	result = []
	response = None

	if host and token:
		response = request.get(host + '/apps', headers = create_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		for application in data:
			if 'id' in application:
				result.append(application['id'])
	return result


def create_headers(token : str) -> Headers:
	return\
	{
		'Accept': 'application/vnd.heroku+json;version=3',
		'Authorization': 'Bearer ' + token
	}
