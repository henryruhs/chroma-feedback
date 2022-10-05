from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, request
from chroma_feedback.typing import Headers, Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--datadog-host', default = 'https://api.datadoghq.com')
		program.add_argument('--datadog-slug', action = 'append', required = True)
		program.add_argument('--datadog-api-key', required = True)
		program.add_argument('--datadog-application-key', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	for slug in ARGS.datadog_slug:
		result.extend(fetch(ARGS.datadog_host, slug, ARGS.datadog_api_key, ARGS.datadog_application_key))
	return result


def fetch(host : str, slug : str, api_key : str, application_key : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and api_key and application_key:
		response = request.get(host + '/api/v1/monitor/' + slug, headers = create_headers(api_key, application_key))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'name' in data and 'overall_state' in data:
			result.append(normalize_data(data['name'], data['overall_state']))
	return result


def create_headers(api_key : str, application_key : str) -> Headers:
	return \
	{
		'Accept': 'application/json',
		'DD-API-KEY': api_key,
		'DD-APPLICATION-KEY': application_key
	}
