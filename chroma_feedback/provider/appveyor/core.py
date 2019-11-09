from typing import Any, Dict, List
import argparse
import requests
from chroma_feedback import helper
from .normalize import normalize_data

ARGS = None


def init(program : argparse.ArgumentParser) -> None:
	global ARGS


	if not ARGS:
		program.add_argument('--appveyor-host', default = 'https://ci.appveyor.com')
		program.add_argument('--appveyor-slug', action = 'append')
		program.add_argument('--appveyor-token')
	ARGS = program.parse_known_args()[0]


def run() -> List[Dict[str, Any]]:
	result = []

	if ARGS.appveyor_slug:
		for slug in ARGS.appveyor_slug:
			result.extend(fetch(ARGS.appveyor_host, slug, None))
	else:
		result.extend(fetch(ARGS.appveyor_host, None, ARGS.appveyor_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Dict[str, Any]]:
	response = None

	if host and slug:
		response = requests.get(host + '/api/projects/' + slug)
	elif host and token:
		response = requests.get(host + '/api/projects', headers =
		{
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if data and data['project'] and data['build']:
			return\
			[
				normalize_data(data['project'], data['build'])
			]
		if data:
			result = []

			for project in data:
				if project['builds'] and project['builds'][0]:
					result.append(normalize_data(project, project['builds'][0]))
			return result
	return []
