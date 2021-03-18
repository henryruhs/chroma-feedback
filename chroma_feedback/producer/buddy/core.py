from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--buddy-host', default = 'https://api.buddy.works')
		program.add_argument('--buddy-slug', action = 'append', required = True)
		program.add_argument('--buddy-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	for slug in ARGS.buddy_slug:
		result.extend(fetch(ARGS.buddy_host, slug, ARGS.buddy_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug and token:
		slug_list = slug.split('/')
		response = request.get(host + '/workspaces/' + slug_list[0] + '/projects/' + slug_list[1] + '/pipelines/', headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'pipelines' in data:
			pipeline = helper.get_first(data['pipelines'])

			if pipeline and 'last_execution_status' in pipeline:
				result.append(normalize_data(slug, pipeline['last_execution_status']))
	return result
