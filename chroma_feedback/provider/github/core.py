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
		program.add_argument('--github-token', required = True)
	args = program.parse_known_args()[0]


def run():
	result = []

	for slug in args.github_slug:
		result.extend(fetch(args.github_host, slug, args.github_username, args.github_token))
	return result


def fetch(host, slug, username, token):
	response = None

	if host and slug and username and token:
		username_token = username + ':' + token
		response = requests.get(host + '/repos/' + slug + '/status/master', headers =
		{
			'Authorization': 'Basic ' + base64.b64encode(username_token.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()

		if data:
			return normalize_data(data)
	return []
