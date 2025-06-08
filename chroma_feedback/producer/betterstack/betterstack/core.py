from argparse import ArgumentParser
from typing import List, Optional, cast

from chroma_feedback import request
from chroma_feedback.types import Headers, Producer
from .normalize import normalize_data
from .types import Args

ARGS : Optional[Args] = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--betterstack-host', default = 'https://uptime.betterstack.com')
		program.add_argument('--betterstack-slug', action = 'append')
		program.add_argument('--betterstack-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	if ARGS.get('betterstack_slug'):
		for slug in ARGS.get('betterstack_slug'):
			result.extend(fetch(ARGS.get('betterstack_host'), slug, ARGS.get('betterstack_token')))
	else:
		result.extend(fetch(ARGS.get('betterstack_host'), None, ARGS.get('betterstack_token')))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/api/v2/monitors?=pronounceable_name=' + slug, headers = create_headers(token))
	elif host and token:
		response = request.get(host + '/api/v2/monitors', headers = create_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'data' in data:
			for monitor in data['data']:
				if 'attributes' in monitor and 'pronounceable_name' in monitor['attributes'] and 'url' in monitor['attributes'] and 'status' in monitor['attributes']:
					result.append(normalize_data(monitor['attributes']['pronounceable_name'], monitor['attributes']['url'], monitor['attributes']['status']))
	return result


def create_headers(token : str) -> Headers:
	return\
	{
		'Accept': 'application/json',
		'Authorization': 'Bearer ' + token
	}
