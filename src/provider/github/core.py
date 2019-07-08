import base64
import requests
from .normalize import normalize_data

args = None


def init(program):
	global args

	if not args:
		program.add_argument('--github-host', default = 'https://api.github.com')
		program.add_argument('--github-slug', action = 'append', required = True)
		program.add_argument('--github-username', required = True)
		program.add_argument('--github-password', required = True)
	args = program.parse_known_args()[0]


def run():
	host = args.github_host
	slugs = args.github_slug
	username = args.github_username
	password = args.github_password
	result = []

	for slug in slugs:
		result.extend(fetch(host, slug, username, password))
	return result


def fetch(host, slug, username, password):
	response = None

	if host and slug and username and password:
		username_password = username + ':' + password
		response = requests.get(host + '/repos/' + slug + '/status/master', headers =
		{
			'Authorization': 'Basic ' + base64.b64encode(username_password.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()

		if data:
			return normalize_data(data)
	return []
