from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--bitbucket-host', default = 'https://api.bitbucket.org')
		program.add_argument('--bitbucket-slug', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	for slug in ARGS.bitbucket_slug:
		result.extend(fetch(ARGS.bitbucket_host, slug))
	return result


def fetch(host : str, slug : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug:
		response = request.get(host + '/2.0/repositories/' + slug + '/pipelines/', headers =
		{
			'Accept': 'application/json'
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'values' in data:
			build = helper.get_first(data['values'])
			if build:
				result.append(normalize_data(build))
	return result
