from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--circle-host', default = 'https://circleci.com')
		program.add_argument('--circle-organization')
		program.add_argument('--circle-slug', action = 'append')
		program.add_argument('--circle-filter')
		program.add_argument('--circle-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	if ARGS.circle_slug:
		for slug in ARGS.circle_slug:
			result.extend(fetch(ARGS.circle_host, None, slug, ARGS.circle_filter, ARGS.circle_token))
	elif ARGS.circle_organization:
		result.extend(fetch(ARGS.circle_host, ARGS.circle_organization, None, None, ARGS.circle_token))
	return result


def fetch(host : str, organization : str, slug : str, filter : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug and filter == 'mine' and token:
		response = request.get(host + '/api/v2/project/' + slug + '/pipeline/mine', headers =
		{
			'Accept': 'application/json',
			'Circle-Token': token
		})
	elif host and slug and token:
		response = request.get(host + '/api/v2/project/' + slug + '/pipeline', headers =
		{
			'Accept': 'application/json',
			'Circle-Token': token
		})
	elif host and organization and token:
		response = request.get(host + '/api/v2/pipeline?org-slug=' + organization, headers =
		{
			'Accept': 'application/json',
			'Circle-Token': token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'items' in data:
			pipeline = helper.get_first(data['items'])
			if 'id' in pipeline:
				result.extend(fetch_workflows(host, pipeline['id'], token))
	return result


def fetch_workflows(host : str, pipeline_id : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and pipeline_id and token:
		response = request.get(host + '/api/v2/pipeline/' + pipeline_id + '/workflow', headers =
		{
			'Accept': 'application/json',
			'Circle-Token': token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'items' in data:
			for build in data['items']:
				result.append(normalize_data(build))
	return result
