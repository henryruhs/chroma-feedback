from typing import List
from argparse import ArgumentParser
import base64
from chroma_feedback import helper, request
from chroma_feedback.typing import ProducerModel
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--azure-host', default = 'https://dev.azure.com')
		program.add_argument('--azure-slug', action = 'append')
		program.add_argument('--azure-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[ProducerModel]:
	result = []

	if ARGS.azure_slug:
		for slug in ARGS.azure_slug:
			result.extend(fetch(ARGS.azure_host, slug, ARGS.azure_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[ProducerModel]:
	result = []
	response = None

	if host and slug and token:
		token = ':' + token
		response = request.get(host + '/' + slug + '/_apis/build/builds?api-version=6.0', headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Basic ' + base64.b64encode(token.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'value' in data:
			build = helper.get_first(data['value'])

			if 'project' in build and 'name' in build['project'] and 'status' in build:
				if 'result' in build:
					result.append(normalize_data(build['project']['name'], build['status'], build['result']))
				else:
					result.append(normalize_data(build['project']['name'], build['status'], None))
	return result
