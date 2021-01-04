from typing import Any, Dict, List
from argparse import ArgumentParser
import base64
from chroma_feedback import helper, request
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--jenkins-host', required = True)
		program.add_argument('--jenkins-slug', action = 'append', required = True)
		program.add_argument('--jenkins-username', required = True)
		program.add_argument('--jenkins-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	for slug in ARGS.jenkins_slug:
		result.extend(fetch(ARGS.jenkins_host, slug, ARGS.jenkins_username, ARGS.jenkins_token))
	return result


def fetch(host : str, slug : str, username : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug and username and token:
		username_token = username + ':' + token
		response = request.get(host + '/job/' + slug + '/lastBuild/api/json', headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Basic ' + base64.b64encode(username_token.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if data:
			data['slug'] = slug
			result.append(normalize_data(data))
	return result
