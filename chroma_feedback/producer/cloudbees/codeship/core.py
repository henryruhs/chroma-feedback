from argparse import ArgumentParser
from typing import Any, List

from chroma_feedback import helper, request
from chroma_feedback.typing import Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--cloudbees-codeship-host', default = 'https://api.codeship.com')
		program.add_argument('--cloudbees-codeship-slug', action = 'append')
		program.add_argument('--cloudbees-codeship-username', required = True)
		program.add_argument('--cloudbees-codeship-password', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []
	auth = fetch_auth(ARGS.cloudbees_codeship_host, ARGS.cloudbees_codeship_username, ARGS.cloudbees_codeship_password)

	if 'access_token' in auth and 'organizations' in auth:
		for organization in auth['organizations']:
			projects = fetch_projects(ARGS.cloudbees_codeship_host, organization['uuid'], auth['access_token'])

			if projects:
				for project in projects:
					if ARGS.cloudbees_codeship_slug is None or project['name'] in ARGS.cloudbees_codeship_slug:
						result.extend(fetch(ARGS.cloudbees_codeship_host, organization['uuid'], project['name'], project['uuid'], auth['access_token']))
	return result


def fetch(host : str, organization_id : str, project_name : str, project_id : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and organization_id and project_id and token:
		response = request.get(host + '/v2/organizations/' + organization_id + '/projects/' + project_id + '/builds', headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'builds' in data:
			build = helper.get_first(data['builds'])

			if build and 'status' in build:
				result.append(normalize_data(project_name, build['status']))
	return result


def fetch_auth(host : str, username : str, password : str) -> Any:
	result = {}
	response = None

	if host and username and password:
		response = request.post(host + '/v2/auth', headers = request.create_basic_auth_headers(username, password))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'access_token' in data and 'organizations' in data:
			result['token'] = data['access_token']
			result['organizations'] = data['organizations']
	return result


def fetch_projects(host : str, organization_id : str, token : str) -> List[Any]:
	result = []
	response = None

	if host and organization_id and token:
		response = request.get(host + '/v2/organizations/' + organization_id + '/projects', headers = request.create_bearer_auth_headers(token))

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'projects' in data:
			for project in data['projects']:
				result.append(project)
	return result
