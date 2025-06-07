from argparse import ArgumentParser
from typing import Any, List, Optional, cast

from chroma_feedback import request
from chroma_feedback.types import Headers, Producer
from .normalize import normalize_data
from .types import Args

ARGS : Optional[Args] = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--travis-host', default = 'https://api.travis-ci.com')
		program.add_argument('--travis-slug', action = 'append', required = True)
		program.add_argument('--travis-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	for slug in ARGS.get('travis_slug'):
		result.extend(fetch(ARGS.get('travis_host'), slug, ARGS.get('travis_token')))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/repos/' + slug, headers = create_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'repo' in data:
			result.append(_normalize_data(data['repo']))
		elif 'repos' in data:
			for repository in data['repos']:
				result.append(_normalize_data(repository))
	return result


def _normalize_data(repository : Any) -> Optional[Producer]:
	if 'slug' in repository and 'last_build_state' in repository and 'active' in repository:
		return normalize_data(repository['slug'], repository['last_build_state'], repository['active'])
	return None


def create_headers(token : str) -> Headers:
	return\
	{
		'Accept': 'application/vnd.travis-ci.2.1+json',
		'Authorization': 'Token ' + token
	}
