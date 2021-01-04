from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--gitlab-host', default = 'https://gitlab.com')
		program.add_argument('--gitlab-slug', action = 'append', required = True)
		program.add_argument('--gitlab-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	for slug in ARGS.gitlab_slug:
		result.extend(fetch(ARGS.gitlab_host, slug, ARGS.gitlab_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/api/v4/projects/' + slug + '/pipelines', headers =
		{
			'Accept': 'application/json',
			'Private-Token': token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)
		pipeline = helper.get_first(data)

		if 'id' in pipeline:
			pipeline_id = str(pipeline['id'])
			result.extend(fetch_jobs(host, slug, pipeline_id, token))
	return result


def fetch_jobs(host : str, slug : str, pipeline_id : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug and pipeline_id and token:
		response = request.get(host + '/api/v4/projects/' + slug + '/pipelines/' + pipeline_id + '/jobs', headers =
		{
			'Accept': 'application/json',
			'Private-Token': token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		for build in data:
			build['slug'] = slug
			result.append(normalize_data(build))
	return result
