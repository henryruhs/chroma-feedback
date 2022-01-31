from typing import List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from chroma_feedback.typing import Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--custom-host', default = 'http://localhost')
		program.add_argument('--custom-slug', action = 'append', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	for slug in ARGS.custom_slug:
		result.extend(fetch(ARGS.custom_host, slug))
	return result


def fetch(host : str, slug : str) -> List[Producer]:
	result = []
	response = None

	if host and slug:
		response = request.get(host + '/statuses/' + slug, headers =
		{
			'Accept': 'application/json'
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if data:
			for build in data:
				if 'slug' in build and 'url' in build and 'status' in build:
					result.append(normalize_data(build['slug'], build['url'], build['status']))
	return result
