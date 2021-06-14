from typing import List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from chroma_feedback.typing import ProducerModel
from .normalize import normalize_data, normalize_slug

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--bamboo-host', required = True)
		program.add_argument('--bamboo-slug', action = 'append', required = True)
		program.add_argument('--bamboo-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[ProducerModel]:
	result = []

	for slug in ARGS.bamboo_slug:
		result.extend(fetch(ARGS.bamboo_host, slug, ARGS.bamboo_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[ProducerModel]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/rest/api/latest/result/' + normalize_slug(slug), headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'results' in data and 'result' in data['results']:
			for project in data['results']['result']:
				if 'key' in project and 'buildState' in project:
					result.append(normalize_data(project['key'], project['buildState']))
		elif 'key' in data and 'buildState' in data:
			result.append(normalize_data(data['key'], data['buildState']))
	return result
