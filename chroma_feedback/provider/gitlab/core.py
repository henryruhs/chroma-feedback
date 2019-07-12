import requests
from .normalize import normalize_data

args = None


def init(program):
	global args

	if not args:
		program.add_argument('--gitlab-host', default = 'https://gitlab.com')
		program.add_argument('--gitlab-slug', action = 'append', required = True)
		program.add_argument('--gitlab-token', required = True)
	args = program.parse_known_args()[0]


def run():
	result = []

	for slug in args.gitlab_slug:
		result.extend(fetch(args.gitlab_host, slug, args.gitlab_token))
	return result


def fetch(host, slug, token):
	response = None

	if host and slug and token:
		response = requests.get(host + '/api/v4/projects/' + slug + '/pipelines', headers =
		{
			'Private-Token': token
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()

		if data and data[0] and 'id' in data[0]:
			return fetch_jobs(host, slug, str(data[0]['id']), token)
	return []


def fetch_jobs(host, slug, pipeline, token):
	response = None

	if host and slug and pipeline and token:
		response = requests.get(host + '/api/v4/projects/' + slug + '/pipelines/' + pipeline + '/jobs', headers =
		{
			'Private-Token': token
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()
		result = []

		for project in data:
			project['slug'] = slug
			result.extend(normalize_data(project))
		return result
	return []
