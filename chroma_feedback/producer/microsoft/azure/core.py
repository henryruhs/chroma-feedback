from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, request
from chroma_feedback.typing import Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--microsoft-azure-host', default = 'https://dev.azure.com')
		program.add_argument('--microsoft-azure-slug', action = 'append', required = True)
		program.add_argument('--microsoft-azure-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	for slug in ARGS.microsoft_azure_slug:
		result.extend(fetch(ARGS.microsoft_azure_host, slug, ARGS.microsoft_azure_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/' + slug + '/_apis/build/builds?api-version=6.0', headers = request.create_basic_auth_headers('', token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'value' in data:
			build = helper.get_first(data['value'])

			if build and 'project' in build and 'name' in build['project'] and 'status' in build:
				if 'result' in build:
					result.append(normalize_data(build['project']['name'], build['status'], build['result']))
				else:
					result.append(normalize_data(build['project']['name'], build['status'], None))
	return result
