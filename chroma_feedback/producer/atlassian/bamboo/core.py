from argparse import ArgumentParser
from typing import List, Optional, cast

from chroma_feedback import request
from chroma_feedback.types import Producer
from .normalize import normalize_data, normalize_slug
from .types import Args

ARGS : Optional[Args] = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--atlassian-bamboo-host', required = True)
		program.add_argument('--atlassian-bamboo-slug', action = 'append', required = True)
		program.add_argument('--atlassian-bamboo-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	for slug in ARGS.get('atlassian_bamboo_slug'):
		result.extend(fetch(ARGS.get('atlassian_bamboo_host'), slug, ARGS.get('atlassian_bamboo_token')))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		slug = normalize_slug(slug)
		response = request.get(host + '/rest/api/latest/result/' + slug, headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'results' in data and 'result' in data['results']:
			for project in data['results']['result']:
				if 'key' in project and 'buildState' in project:
					result.append(normalize_data(project['key'], project['buildState']))
		elif 'key' in data and 'buildState' in data:
			result.append(normalize_data(data['key'], data['buildState']))
	return result
