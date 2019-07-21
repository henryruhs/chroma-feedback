import requests
from chroma_feedback import helper
from .normalize import normalize_data

ARGS = None


def init(program):
	global ARGS

	if not ARGS:
		program.add_argument('--travis-host', default = 'https://api.travis-ci.org')
		program.add_argument('--travis-slug', action = 'append', required = True)
	ARGS = program.parse_known_args()[0]


def run():
	result = []

	for slug in ARGS.travis_slug:
		result.extend(fetch(ARGS.travis_host, slug))
	return result


def fetch(host, slug):
	response = None

	if host and slug:
		response = requests.get(host + '/repos/' + slug, headers =
		{
			'Accept': 'application/vnd.travis-ci.2.1+json'
		})

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if 'repo' in data:
			return normalize_data(data['repo'])
		if 'repos' in data:
			result = []
			for project in data['repos']:
				result.extend(normalize_data(project))
			return result
	return []
