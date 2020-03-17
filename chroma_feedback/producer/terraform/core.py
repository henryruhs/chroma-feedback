from typing import Any, Dict, List
from argparse import ArgumentParser
import os
import requests
from chroma_feedback import helper
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--terraform-host', default = 'https://app.terraform.io')
		program.add_argument('--terraform-slug', action = 'append', required = True)
		program.add_argument('--terraform-token', default = os.environ['TFE_TOKEN'])
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Dict[str, Any]]:
	result = []

	for slug in ARGS.terraform_slug:
		result.extend(fetch(ARGS.terraform_host, slug, ARGS.terraform_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Dict[str, Any]]:
	result = []
	response = None

	if host and slug and token:
		api = parse_slug(slug)
		headers = {
			'Content-Type': 'application/vnd.api+json',
			'Authorization': "Bearer " + token
		}
		params = {
			'include': 'current_run'
		}
		response = requests.get(host + '/api/v2' + api, params = params, headers = headers)

	# process response
	if response and response.status_code == 200:
		json = helper.parse_json(response)
		if 'data' in json and 'included' in json:
			if isinstance(json['data'], dict):
				# Single result, either ws ID or name
				data = {
					'id': slug,
					'status': json['included'][0]['attributes']['status']
				}
				result.append(normalize_data(data))
			if isinstance(json['data'], list):
				wsnames = [ sub['attributes']['name'] for sub in json['data'] ]
				wsstatuses = [ sub['attributes']['status'] for sub in json['included'] ]
				for workspace, status in zip(wsnames, wsstatuses):
					data = {
						'id': slug + "/" + workspace,
						'status': status
					}
					result.append(normalize_data(data))

	return result


def parse_slug(slug : str) -> str:
	if slug:
		tokens = slug.split('/')
		if len(tokens) == 1:
			if tokens[0].startswith('ws-'):  # It's a workspace ID
				organization = ""
				workspace = "/workspaces/" + tokens[0]
			else: # It's a whole organization
				organization = "/organizations/" + tokens[0]
				workspace = "/workspaces"
		else:
			organization = "/organizations/" + tokens[0]
			workspace = "/workspaces/" + tokens[1]
			# If there are more than two tokens it's a mistake.

		return organization + workspace
	return None
