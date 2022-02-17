from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, request
from chroma_feedback.typing import Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--wercker-host', default = 'https://app.wercker.com')
		program.add_argument('--wercker-slug', action = 'append', required = True)
		program.add_argument('--wercker-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	for slug in ARGS.wercker_slug:
		application_ids = fetch_application_ids(ARGS.wercker_host, slug, ARGS.wercker_token)

		for application_id in application_ids:
			result.extend(fetch(ARGS.wercker_host, slug, application_id, ARGS.wercker_token))
	return result


def fetch(host : str, slug : str, application_id : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and application_id and token:
		response = request.get(host + '/api/v3/runs?applicationId=' + application_id, headers = request.create_bearer_auth_headers(token))

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)
		build = helper.get_first(data)

		if build and 'status' in build and 'result' in build:
			result.append(normalize_data(slug, build['status'], build['result']))
	return result


def fetch_application_ids(host : str, slug : str, token : str) -> List[str]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/api/v3/applications/' + slug, headers = request.create_bearer_auth_headers(token))

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'id' in data:
			result.append(data['id'])
		else:
			for application in data:
				if 'id' in application:
					result.append(application['id'])
	return result
