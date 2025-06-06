from argparse import ArgumentParser
from typing import List, Optional, cast

from chroma_feedback import helper, request
from chroma_feedback.types import Headers, Producer
from .normalize import normalize_data
from .types import Args

ARGS : Optional[Args] = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--gitlab-host', default = 'https://gitlab.com')
		program.add_argument('--gitlab-slug', action = 'append')
		program.add_argument('--gitlab-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	if ARGS.get('gitlab_slug'):
		for slug in ARGS.get('gitlab_slug'):
			pipeline_ids = fetch_pipeline_ids(ARGS.get('gitlab_host'), slug, ARGS.get('gitlab_token'))

			if pipeline_ids:
				for pipeline_id in pipeline_ids:
					result.extend(fetch(ARGS.get('gitlab_host'), slug, pipeline_id, ARGS.get('gitlab_token')))
	else:
		project_ids = fetch_project_ids(ARGS.get('gitlab_host'), ARGS.get('gitlab_token'))

		for project_id in project_ids:
			pipeline_ids = fetch_pipeline_ids(ARGS.get('gitlab_host'), project_id, ARGS.get('gitlab_token'))

			if pipeline_ids:
				for pipeline_id in pipeline_ids:
					result.extend(fetch(ARGS.get('gitlab_host'), project_id, pipeline_id, ARGS.get('gitlab_token')))
	return result


def fetch(host : str, slug : str, pipeline_id : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and pipeline_id and token:
		response = request.get(host + '/api/v4/projects/' + slug + '/pipelines/' + pipeline_id + '/jobs', headers = create_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		for build in data:
			if 'name' in build and 'web_url' in build and 'status' in build:
				result.append(normalize_data(slug + '/' + build['name'], build['web_url'], build['status']))
	return result


def fetch_project_ids(host : str, token : str) -> List[str]:
	result = []
	response = None

	if host and token:
		response = request.get(host + '/api/v4/projects?owned=true', headers = create_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		for project in data:
			if 'id' in project:
				result.append(str(project['id']))
	return result


def fetch_pipeline_ids(host : str, slug : str, token : str) -> List[str]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/api/v4/projects/' + slug + '/pipelines', headers = create_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)
		pipeline = helper.get_first(data)

		if pipeline and 'id' in pipeline:
			result.append(str(pipeline['id']))
	return result


def create_headers(token : str) -> Headers:
	return\
	{
		'Accept': 'application/json',
		'Private-Token': token
	}
