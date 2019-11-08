import base64
import requests
from chroma_feedback import helper
from .normalize import normalize_data

ARGS = None


def init(program):
	global ARGS

	if not ARGS:
		program.add_argument('--codeship-host', default = 'https://api.codeship.com')
		program.add_argument('--codeship-slug', action = 'append')
		program.add_argument('--codeship-username', required = True)
		program.add_argument('--codeship-password', required = True)
	ARGS = program.parse_known_args()[0]


def run():
	result = []
	auth = fetch_auth(ARGS.codeship_host, ARGS.codeship_username, ARGS.codeship_password)

	for organization in auth['organizations']:
		result.extend(fetch(ARGS.codeship_host, organization['uuid'], ARGS.codeship_slug, auth['access_token']))
	return result


def fetch(host, organization, slug, token):
	response = None

	if host and organization and token:
		response = requests.get(host + '/v2/organizations/' + organization + '/projects', headers =
		{
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)
		result = []

		for project in data['projects']:
			if not slug or str(project['id']) in slug:
				result.extend(fetch_builds(host, organization, project['uuid'], token))
		return result
	return []


def fetch_builds(host, organization, project, token):
	response = None

	if host and organization and project and token:
		response = requests.get(host + '/v2/organizations/' + organization + '/projects/' + project + '/builds', headers =
		{
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if data['builds']:
			return normalize_data(data['builds'][0])
	return []


def fetch_auth(host, username, password):
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

		if data:
			return data
	return None
