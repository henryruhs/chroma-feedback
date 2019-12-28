from typing import Any, Dict, List
from argparse import ArgumentParser
import base64
import requests
from chroma_feedback import helper
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--codeship-host', default = 'https://api.codeship.com')
		program.add_argument('--codeship-slug', action = 'append')
		program.add_argument('--codeship-username', required = True)
		program.add_argument('--codeship-password', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []
	auth = fetch_auth(ARGS.codeship_host, ARGS.codeship_username, ARGS.codeship_password)

	for organization in auth['organizations']:
		result.extend(fetch(ARGS.codeship_host, organization['uuid'], ARGS.codeship_slug, auth['token']))
	return result


def fetch(host : str, organization : str, slug : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and organization and token:
		response = requests.get(host + '/v2/organizations/' + organization + '/projects', headers =
		{
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		for project in data['projects']:
			project_id = str(project['id'])
			if not slug or project_id in slug:
				result.extend(fetch_builds(host, organization, project['uuid'], token))
	return result


def fetch_builds(host : str, organization : str, project : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and organization and project and token:
		response = requests.get(host + '/v2/organizations/' + organization + '/projects/' + project + '/builds', headers =
		{
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if 'builds' in data:
			build = helper.get_first(data['builds'])
			if build:
				result.append(normalize_data(build))
	return result


def fetch_auth(host : str, username : str, password : str) -> Dict[str, Any]:
	result = {}
	response = None

	if host and username and password:
		username_token = username + ':' + password
		response = requests.post(host + '/v2/auth', headers =
		{
			'Authorization': 'Basic ' + base64.b64encode(username_token.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if 'access_token' and 'organizations' in data:
			result['token'] = data['access_token']
			result['organizations'] = data['organizations']
	return result
