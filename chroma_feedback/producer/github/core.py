from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from chroma_feedback.typing import ProducerModel
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--github-host', default = 'https://api.github.com')
		program.add_argument('--github-slug', action = 'append', required = True)
		program.add_argument('--github-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[ProducerModel]:
	result = []

	for slug in ARGS.github_slug:
		result.extend(fetch(ARGS.github_host, slug, ARGS.github_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[ProducerModel]:
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


def fetch_repositories(host : str, username : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and username and token:
		response = request.get(host + '/users/' + username + '/repos', headers =
		{
			'Accept': 'application/vnd.github.v3+json',
			'Authorization': 'Token ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if data:
			for repository in data:
				result.append(repository)
	return result


def fetch_runs(host : str, slug : str, token : str) -> List[ProducerModel]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/repos/' + slug + '/actions/runs', headers =
		{
			'Accept': 'application/vnd.github.v3+json',
			'Authorization': 'Token ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'workflow_runs' in data:
			build = helper.get_first(data['workflow_runs'])

			if build and 'repository' in build and 'full_name' in build['repository'] and 'status' in build and 'conclusion' in build:
				result.append(normalize_data(build['repository']['full_name'], build['status'], build['conclusion']))
	return result
