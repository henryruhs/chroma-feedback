from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, request
from chroma_feedback.typing import Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--jenkins-host', required = True)
		program.add_argument('--jenkins-slug', action = 'append', required = True)
		program.add_argument('--jenkins-username', required = True)
		program.add_argument('--jenkins-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	for slug in ARGS.jenkins_slug:
		result.extend(fetch(ARGS.jenkins_host, slug, ARGS.jenkins_username, ARGS.jenkins_token))
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
