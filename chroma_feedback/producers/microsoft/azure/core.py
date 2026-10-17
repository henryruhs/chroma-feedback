from argparse import ArgumentParser
from typing import List, Optional, cast

from chroma_feedback import helper, request
from chroma_feedback.types import Producer
from .normalize import normalize_data
from .types import Args

ARGS : Optional[Args] = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--microsoft-azure-host', default = 'https://dev.azure.com')
		program.add_argument('--microsoft-azure-slug', action = 'append', required = True)
		program.add_argument('--microsoft-azure-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	for slug in ARGS.get('microsoft_azure_slug'):
		result.extend(fetch(ARGS.get('microsoft_azure_host'), slug, ARGS.get('microsoft_azure_token')))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/' + slug + '/_apis/build/builds?api-version=7.1', headers = request.create_basic_auth_headers('', token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'value' in data:
			build = helper.get_first(data.get('value'))

			data_project = helper.deep_get(build, [ 'project', 'name' ])
			data_status = helper.deep_get(build, [ 'status' ])

			if build and data_project and data_status:
				data_result = helper.deep_get(build, [ 'result' ])

				if data_result:
					result.append(normalize_data(data_project, data_status, data_result))
				else:
					result.append(normalize_data(data_project, data_status, None))
	return result
