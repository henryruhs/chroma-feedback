import base64
import requests
from chroma_feedback import helper
from .normalize import normalize_data

args = None


def init(program):
	global args

	if not args:
		program.add_argument('--circle-host', default = 'https://circleci.com')
		program.add_argument('--circle-slug', action = 'append')
		program.add_argument('--circle-token')
	args = program.parse_known_args()[0]


def run():
	result = []

	if args.circle_slug:
		for slug in args.circle_slug:
			result.extend(fetch(args.circle_host, slug, None))
	else:
		result.extend(fetch(args.circle_host, None, args.circle_token))
	return result


def fetch(host, slug, token):
	response = None

	if host and slug:
		response = requests.get(host + '/api/v1.1/project/' + slug)
	elif host and token:
		response = requests.get(host + '/api/v1.1/recent-builds', headers =
		{
			'Authorization': 'Basic ' + base64.b64encode(token.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		for project in data:
			return normalize_data(project)
	return []
