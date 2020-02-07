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
		program.add_argument('--bamboo-host', required = True)
		program.add_argument('--bamboo-slug', action = 'append', required = True)
		program.add_argument('--bamboo-username', required = True)
		program.add_argument('--bamboo-password', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	for slug in ARGS.bamboo_slug:
		result.extend(fetch(ARGS.bamboo_host, slug, ARGS.bamboo_username, ARGS.bamboo_password))
	return result


def fetch(host : str, slug : str, username : str, password : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug and username and password:
		username_password = username + ':' + password
		response = requests.get(host + '/rest/api/latest/result/' + slug + ("-latest" if "-" in slug else ''), headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Basic ' + base64.b64encode(username_password.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if 'results' in data and 'result' in data['results']:
			for plan in data['results']['result']:
				result.append(normalize_data(plan))
		else:
			result.append(normalize_data(data))

	return result
