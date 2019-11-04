import base64
import requests
from chroma_feedback import helper
from .normalize import normalize_data

ARGS = None


def init(program):
	global ARGS

	if not ARGS:
		program.add_argument('--codeship-host', default = 'https://api.codeship.com')
		program.add_argument('--codeship-organization', required = True)
		program.add_argument('--codeship-project', action = 'append', required = True)
		program.add_argument('--codeship-username', required = True)
		program.add_argument('--codeship-password', required = True)
	ARGS = program.parse_known_args()[0]


def run():
	result = []
	token = fetch_token(ARGS.codeship_host, ARGS.codeship_username, ARGS.codeship_password)

	if token:
		for project in ARGS.codeship_project:
			result.extend(fetch(ARGS.codeship_host, ARGS.codeship_organization, project, token))
	return result


def fetch(host, organization, project, token):
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
			return normalize_data(data['builds'][0])
	return []


def fetch_token(host, username, password):
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

		if data['access_token']:
			return data['access_token']
	return None
