from argparse import ArgumentParser
from typing import Any, Dict, List

from chroma_feedback import helper, request
from chroma_feedback.typing import Headers, Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--github-host', default = 'https://api.github.com')
		program.add_argument('--github-slug', action = 'append', required = True)
		program.add_argument('--github-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	for slug in ARGS.github_slug:
		result.extend(fetch(ARGS.github_host, slug, ARGS.github_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	SLUG = helper.parse_slug(slug)
	repositories = None

	if 'workspace' in SLUG and 'project' not in SLUG:
		repositories = fetch_repositories(host, SLUG['workspace'], token)

	if repositories:
		for repository in repositories:
			if 'full_name' in repository:
				result.extend(fetch_runs(host, repository['full_name'], token))
	elif 'workspace' in SLUG and 'project' in SLUG:
		result.extend(fetch_runs(host, SLUG['workspace'] + '/' + SLUG['project'], token))
	return result


def fetch_repositories(host : str, username : str, token : str) -> List[Any]:
	result = []
	response = None

	if host and username and token:
		response = request.get(host + '/users/' + username + '/repos', headers = _create_headers(token))

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		for repository in data:
			result.append(repository)
	return result


def fetch_runs(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/repos/' + slug + '/actions/runs', headers = _create_headers(token))

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'workflow_runs' in data:
			build = helper.get_first(data['workflow_runs'])

			if build and 'repository' in build and 'full_name' in build['repository'] and 'html_url' in build and 'status' in build and 'conclusion' in build:
				result.append(normalize_data(build['repository']['full_name'], build['html_url'], build['status'], build['conclusion']))
	return result


def _create_headers(token : str) -> Headers:
	return\
	{
		'Accept': 'application/vnd.github.v3+json',
		'Authorization': 'Token ' + token
	}
