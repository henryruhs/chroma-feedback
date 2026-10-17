from argparse import ArgumentParser
from typing import List, Optional, cast

from chroma_feedback import helper, request
from chroma_feedback.types import Producer
from .normalize import normalize_data, normalize_slug
from .types import Args

ARGS : Optional[Args] = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--atlassian-bamboo-host', required = True)
		program.add_argument('--atlassian-bamboo-slug', action = 'append', required = True)
		program.add_argument('--atlassian-bamboo-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	for slug in ARGS.get('atlassian_bamboo_slug'):
		result.extend(fetch(ARGS.get('atlassian_bamboo_host'), slug, ARGS.get('atlassian_bamboo_token')))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		slug = normalize_slug(slug)
		response = request.get(host + '/rest/api/latest/result/' + slug, headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)
		data_result = helper.deep_get(data, [ 'results', 'result' ])

		if data_result:
			for project in data_result:
				data_slug = project.get('key')
				data_status = project.get('buildState')

				if data_slug and data_status:
					result.append(normalize_data(data_slug, data_status))
		else:
			data_slug = data.get('key')
			data_status = data.get('buildState')

			if data_slug and data_status:
				result.append(normalize_data(data_slug, data_status))
	return result
