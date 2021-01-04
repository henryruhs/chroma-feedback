from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--travis-host', default = 'https://api.travis-ci.com')
		program.add_argument('--travis-slug', action = 'append', required = True)
		program.add_argument('--travis-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	for slug in ARGS.travis_slug:
		result.extend(fetch(ARGS.travis_host, slug, ARGS.travis_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/repos/' + slug, headers =
		{
			'Accept': 'application/vnd.travis-ci.2.1+json',
			'Authorization': 'Token ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'repo' in data:
			result.append(normalize_data(data['repo']))
		if 'repos' in data:
			for project in data['repos']:
				result.append(normalize_data(project))
	return result
