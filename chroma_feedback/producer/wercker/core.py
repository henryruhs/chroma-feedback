from typing import List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from chroma_feedback.typing import ProducerModel
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--wercker-host', default = 'https://app.wercker.com')
		program.add_argument('--wercker-slug', action = 'append', required = True)
		program.add_argument('--wercker-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[ProducerModel]:
	result = []

	for slug in ARGS.wercker_slug:
		result.extend(fetch(ARGS.wercker_host, slug, ARGS.wercker_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[ProducerModel]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/api/v3/applications/' + slug, headers =
		{
			'Accept': 'application/json',
			'Bearer': token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'id' in data:
			result.extend(fetch_runs(host, slug, data['id'], token))
		else:
			for application in data:
				if 'id' in application:
					result.extend(fetch_runs(host, slug, application['id'], token))
	return result


def fetch_runs(host : str, slug : str, application_id : str, token : str) -> List[ProducerModel]:
	result = []
	response = None

	if host and slug and application_id and token:
		response = request.get(host + '/api/v3/runs?applicationId=' + application_id, headers =
		{
			'Accept': 'application/json',
			'Bearer': token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)
		build = helper.get_first(data)

		if build and 'status' in build and 'result' in build:
			result.append(normalize_data(slug, build['status'], build['result']))
	return result
