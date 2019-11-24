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
		program.add_argument('--teamcity-host', default = 'https://teamcity.jetbrains.com')
		program.add_argument('--teamcity-slug', action = 'append')
		program.add_argument('--teamcity-username', required = True)
		program.add_argument('--teamcity-password', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	if ARGS.teamcity_slug:
		for slug in ARGS.teamcity_slug:
			result.extend(fetch(ARGS.teamcity_host, slug, ARGS.teamcity_username, ARGS.teamcity_password))
	else:
		result.extend(fetch(ARGS.teamcity_host, None, ARGS.teamcity_username, ARGS.teamcity_password))
	return result


def fetch(host : str, slug : str, username : str, password : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and username and password:
		username_password = username + ':' + password
		headers =\
		{
			'Accept': 'application/json',
			'Authorization': 'Basic ' + base64.b64encode(username_password.encode('utf-8')).decode('ascii')
		}
		if slug:
			response = requests.get(host + '/app/rest/buildTypes?locator=affectedProject:(id:' + slug + ')&fields=buildType(builds($locator(running:any),build(id,running,status,buildType(id,projectName))))', headers = headers)
		else:
			response = requests.get(host + '/app/rest/buildTypes/?fields=buildType(builds($locator(user:current,running:any),build(id,running,status,buildType(id,projectName))))', headers = headers)

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if 'buildType' in data:
			for project in data['buildType']:
				if 'build' in project['builds']:
					build = helper.get_first(project['builds']['build'])
					result.append(normalize_data(build))
	return result
