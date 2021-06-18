from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from chroma_feedback.typing import ProducerModel
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--buddy-host', default = 'https://api.buddy.works')
		program.add_argument('--buddy-slug', action = 'append', required = True)
		program.add_argument('--buddy-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[ProducerModel]:
	result = []

	for slug in ARGS.buddy_slug:
		result.extend(fetch(ARGS.buddy_host, slug, ARGS.buddy_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[ProducerModel]:
	result = []
	SLUG = helper.parse_slug(slug)
	projects = None

	if 'workspace' in SLUG and 'project' not in SLUG:
		projects = fetch_projects(host, SLUG['workspace'], token)

	if projects:
		for project in projects:
			if 'workspace' in SLUG and 'name' in project:
				result.extend(fetch_pipelines(host, SLUG['workspace'], project['name'], token))
	elif 'workspace' in SLUG and 'project' in SLUG:
		result.extend(fetch_pipelines(host, SLUG['workspace'], SLUG['project'], token))
	return result


def fetch_projects(host : str, workspace : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and workspace and token:
		response = request.get(host + '/workspaces/' + workspace + '/projects', headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'projects' in data:
			for project in data['projects']:
				result.append(project)
	return result


def fetch_pipelines(host: str, workspace: str, project : str, token: str) -> List[ProducerModel]:
	result = []
	response = None

	if host and workspace and project and token:
		response = request.get(host + '/workspaces/' + workspace + '/projects/' + project + '/pipelines/', headers=
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
				result.append(normalize_data(workspace + '/' + project, pipeline['last_execution_status']))
	return result
