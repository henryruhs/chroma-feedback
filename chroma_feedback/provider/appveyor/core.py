import requests
from chroma_feedback import helper
from .normalize import normalize_data

ARGS = None


def init(program):
	global ARGS

	if not ARGS:
		program.add_argument('--appveyor-host', default = 'https://ci.appveyor.com')
		program.add_argument('--appveyor-slug', action = 'append')
		program.add_argument('--appveyor-token')
	ARGS = program.parse_known_args()[0]


def run():
	result = []

	if ARGS.appveyor_slug:
		for slug in ARGS.appveyor_slug:
			result.extend(fetch(ARGS.appveyor_host, slug, None))
	else:
		result.extend(fetch(ARGS.appveyor_host, None, ARGS.appveyor_token))
	return result


def fetch(host, slug, token):
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

		if 'project' and 'build' in data:
			return normalize_data(data['project'], data['build'])
		if data and data[0] and 'builds' in data[0]:
			result = []

			for project in data:
				if project['builds']:
					result.extend(normalize_data(project, project['builds'][0]))
			return result
	return []
