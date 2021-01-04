from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, request
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--github-host', default = 'https://api.github.com')
		program.add_argument('--github-slug', action = 'append', required = True)
		program.add_argument('--github-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	for slug in ARGS.github_slug:
		result.extend(fetch(ARGS.github_host, slug, ARGS.github_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Dict[str, Any]]:
	result = []
	slugs = fetch_slugs(host, slug, token)

	if slugs:
		for __slug__ in slugs:
			result.extend(fetch_runs(host, __slug__, token))
	else:
		result.extend(fetch_runs(host, slug, token))
	return result


def fetch_slugs(host : str, username : str, token : str) -> List[str]:
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
			for project in data:
				if 'full_name' in project:
					result.append(project['full_name'])
	return result


def fetch_runs(host : str, slug : str, token : str) -> List[Dict[str, Any]]:
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
			if build:
				result.append(normalize_data(build))
	return result
