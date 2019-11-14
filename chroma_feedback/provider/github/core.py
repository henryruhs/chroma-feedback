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
		program.add_argument('--github-host', default = 'https://api.github.com')
		program.add_argument('--github-slug', action = 'append', required = True)
		program.add_argument('--github-username', required = True)
		program.add_argument('--github-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	for slug in ARGS.github_slug:
		result.extend(fetch(ARGS.github_host, slug, ARGS.github_username, ARGS.github_token))
	return result


def fetch(host : str, slug : str, username : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug and username and token:
		username_token = username + ':' + token
		response = requests.get(host + '/repos/' + slug + '/status/master', headers =
		{
			'Authorization': 'Basic ' + base64.b64encode(username_token.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if data:
			result.append(normalize_data(data))
	return result
