from argparse import ArgumentParser
from typing import Any, List, Optional, cast

from chroma_feedback import helper, request
from chroma_feedback.types import Producer
from .normalize import normalize_data
from .types import Args

ARGS : Optional[Args] = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--vercel-host', default = 'https://api.vercel.com')
		program.add_argument('--vercel-slug', action = 'append')
		program.add_argument('--vercel-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	if ARGS.get('vercel_slug'):
		for slug in ARGS.get('vercel_slug'):
			result.extend(fetch(ARGS.get('vercel_host'), slug, ARGS.get('vercel_token')))
	else:
		result.extend(fetch(ARGS.get('vercel_host'), None, ARGS.get('vercel_token')))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result : List[Producer] = []
	response = None

	if host and slug and token:
		response = request.get(host + '/v1/projects/' + slug, headers = request.create_bearer_auth_headers(token))
	elif host and token:
		response = request.get(host + '/v1/projects', headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'name' in data and 'latestDeployments' in data:
			result.append(_normalize_data(data))
		else:
			for project in data:
				if 'name' in project and 'latestDeployments' in project:
					result.append(_normalize_data(project))
	return result


def _normalize_data(project : Any) -> Optional[Producer]:
	deployment = helper.get_first(project['latestDeployments'])

	if 'readyState' in deployment:
		return normalize_data(project['name'], deployment['readyState'])
	return None
