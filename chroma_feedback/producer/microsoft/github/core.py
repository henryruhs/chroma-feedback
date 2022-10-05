from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, request
from chroma_feedback.typing import Headers, Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--microsoft-github-host', default = 'https://api.github.com')
		program.add_argument('--microsoft-github-slug', action = 'append', required = True)
		program.add_argument('--microsoft-github-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	for slug in ARGS.microsoft_github_slug:
		slug_fragment = helper.parse_slug(slug)

		if 'workspace' in slug_fragment:
			if 'project' in slug_fragment:
				result.extend(fetch(ARGS.microsoft_github_host, slug_fragment['workspace'] + '/' + slug_fragment['project'], ARGS.microsoft_github_token))
			else:
				repository_names = fetch_repository_names(ARGS.microsoft_github_host, slug_fragment['workspace'], ARGS.microsoft_github_token)

				if repository_names:
					for repository_name in repository_names:
						result.extend(fetch(ARGS.microsoft_github_host, repository_name, ARGS.microsoft_github_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.get(host + '/repos/' + slug + '/actions/runs', headers = create_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'workflow_runs' in data:
			build = helper.get_first(data['workflow_runs'])

			if build and 'repository' in build and 'full_name' in build['repository'] and 'html_url' in build and 'status' in build and 'conclusion' in build:
				result.append(normalize_data(build['repository']['full_name'], build['html_url'], build['status'], build['conclusion']))
	return result


def fetch_repository_names(host : str, username : str, token : str) -> List[str]:
	result = []
	response = None

	if host and username and token:
		response = request.get(host + '/search/repositories?q=user:' + username, headers = create_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'items' in data:
			for repository in data['items']:
				if 'full_name' in repository:
					result.append(repository['full_name'])
	return result


def create_headers(token : str) -> Headers:
	return\
	{
		'Accept': 'application/vnd.github.v3+json',
		'Authorization': 'Token ' + token
	}
