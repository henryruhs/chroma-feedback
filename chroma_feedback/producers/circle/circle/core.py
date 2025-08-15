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
		program.add_argument('--circle-host', default = 'https://circleci.com')
		program.add_argument('--circle-organization')
		program.add_argument('--circle-slug', action = 'append')
		program.add_argument('--circle-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	if ARGS.get('circle_slug'):
		for slug in ARGS.get('circle_slug'):
			pipeline_ids = fetch_pipeline_ids(ARGS.get('circle_host'), None, slug, ARGS.get('circle_token'))

			if pipeline_ids:
				for pipeline_id in pipeline_ids:
					result.extend(fetch(ARGS.get('circle_host'), pipeline_id, ARGS.get('circle_token')))
	elif ARGS.get('circle_organization'):
		pipeline_ids = fetch_pipeline_ids(ARGS.get('circle_host'), ARGS.get('circle_organization'), None, ARGS.get('circle_token'))

		if pipeline_ids:
			for pipeline_id in pipeline_ids:
				result.extend(fetch(ARGS.get('circle_host'), pipeline_id, ARGS.get('circle_token')))
	return result


def fetch(host : str, pipeline_id : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and pipeline_id and token:
		response = request.get(host + '/api/v2/pipeline/' + pipeline_id + '/workflow', headers = create_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'items' in data:
			for build in data['items']:
				if 'project_slug' in build and 'name' in build and 'status' in build:
					result.append(normalize_data(build['project_slug'] + '/' + build['name'], build['status']))
	return result


def fetch_pipeline_ids(host : str, organization : str, slug : str, token : str) -> List[str]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/api/v2/project/' + slug + '/pipeline', headers = create_headers(token))
	elif host and organization and token:
		response = request.get(host + '/api/v2/pipeline?org-slug=' + organization, headers = create_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'items' in data:
			pipeline = helper.get_first(data['items'])

			if pipeline and 'id' in pipeline:
				result.append(pipeline['id'])
	return result


def create_headers(token : str) -> Headers:
	return\
	{
		'Accept': 'application/json',
		'Circle-Token': token
	}
