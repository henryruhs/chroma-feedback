from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, request
from chroma_feedback.typing import Headers, Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--travis-host', default = 'https://api.travis-ci.com')
		program.add_argument('--travis-slug', action = 'append', required = True)
		program.add_argument('--travis-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	for slug in ARGS.travis_slug:
		result.extend(fetch_repositories(ARGS.travis_host, slug, ARGS.travis_token))
	return result


def fetch_repositories(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/repos/' + slug, headers = _create_headers(token))

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'repo' in data and 'slug' in data['repo'] and 'last_build_state' in data['repo'] and 'active' in data['repo']:
			result.append(normalize_data(data['repo']['slug'], data['repo']['last_build_state'], data['repo']['active']))
		if 'repos' in data:
			for repository in data['repos']:
				if 'slug' in repository and 'last_build_state' in repository and 'active' in repository:
					result.append(normalize_data(repository['slug'], repository['last_build_state'], repository['active']))
	return result


def _create_headers(token : str) -> Headers:
	return\
	{
		'Accept': 'application/vnd.travis-ci.2.1+json',
		'Authorization': 'Token ' + token
	}
