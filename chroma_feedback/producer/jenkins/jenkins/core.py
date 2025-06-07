from argparse import ArgumentParser
from typing import List, Optional, cast

from chroma_feedback import request
from chroma_feedback.types import Producer
from .normalize import normalize_data
from .types import Args

ARGS : Optional[Args] = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--jenkins-host', required = True)
		program.add_argument('--jenkins-slug', action = 'append', required = True)
		program.add_argument('--jenkins-username', required = True)
		program.add_argument('--jenkins-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	for slug in ARGS.get('jenkins_slug'):
		result.extend(fetch(ARGS.get('jenkins_host'), slug, ARGS.get('jenkins_username'), ARGS.get('jenkins_token')))
	return result


def fetch(host : str, slug : str, username : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and username and token:
		response = request.get(host + '/job/' + slug + '/lastBuild/api/json', headers = request.create_basic_auth_headers(username, token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'result' in data and 'building' in data:
			result.append(normalize_data(slug, data['result'], data['building']))
	return result
