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
		program.add_argument('--buddy-host', default = 'https://api.buddy.works')
		program.add_argument('--buddy-slug', action = 'append', required = True)
		program.add_argument('--buddy-token', required = True)

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run() -> List[Producer]:
	result = []

	for slug in ARGS.get('buddy_slug'):
		slug_fragment = helper.parse_slug(slug)

		if 'workspace' in slug_fragment:
			if 'project' in slug_fragment:
				result.extend(fetch(ARGS.get('buddy_host'), slug_fragment['workspace'], slug_fragment['project'], ARGS.get('buddy_token')))
			else:
				project_names = fetch_project_names(ARGS.get('buddy_host'), slug_fragment['workspace'], ARGS.get('buddy_token'))

				if project_names:
					for project_name in project_names:
						result.extend(fetch(ARGS.get('buddy_host'), slug_fragment['workspace'], project_name, ARGS.get('buddy_token')))
	return result


def fetch(host: str, workspace: str, project : str, token: str) -> List[Producer]:
	result = []
	response = None

	if host and workspace and project and token:
		response = request.get(host + '/workspaces/' + workspace + '/projects/' + project + '/pipelines/', headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'pipelines' in data:
			pipeline = helper.get_first(data['pipelines'])

			if pipeline and 'last_execution_status' in pipeline:
				result.append(normalize_data(workspace + '/' + project, pipeline['last_execution_status']))
	return result


def fetch_project_names(host : str, workspace : str, token : str) -> List[str]:
	result = []
	response = None

	if host and workspace and token:
		response = request.get(host + '/workspaces/' + workspace + '/projects', headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'projects' in data:
			for project in data['projects']:
				if 'name' in project:
					result.append(project['name'])
	return result

