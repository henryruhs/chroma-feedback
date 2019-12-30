from typing import Any, Dict, List
from argparse import ArgumentParser
import base64
import requests
from chroma_feedback import helper
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--circle-host', default = 'https://circleci.com')
		program.add_argument('--circle-slug', action = 'append')
		program.add_argument('--circle-token')
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	if ARGS.circle_slug:
		for slug in ARGS.circle_slug:
			result.extend(fetch(ARGS.circle_host, slug, None))
	else:
		result.extend(fetch(ARGS.circle_host, None, ARGS.circle_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug:
		response = requests.get(host + '/api/v1.1/project/' + slug)
	elif host and token:
		response = requests.get(host + '/api/v1.1/recent-builds', headers =
		{
			'Authorization': 'Basic ' + base64.b64encode(token.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		for project in data:
			result.append(normalize_data(project))
	return result
