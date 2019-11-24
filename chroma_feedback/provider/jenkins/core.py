from typing import Any, Dict, List
from argparse import ArgumentParser
import requests
from chroma_feedback import helper
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--jenkins-host', required = True)
		program.add_argument('--jenkins-slug', action = 'append', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	for slug in ARGS.jenkins_slug:
		result.extend(fetch(ARGS.jenkins_host, slug))
	return result


def fetch(host : str, slug : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug:
		response = requests.get(host + '/job/' + slug + '/api/json')

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if data:
			result.append(normalize_data(data))
	return result
