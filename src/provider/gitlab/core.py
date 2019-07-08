import requests
from .normalize import normalize_data

args = None


def init(program):
	global args

	if not args:
		program.add_argument('--gitlab-host', default = 'https://gitlab.com')
		program.add_argument('--gitlab-slug', action = 'append', required = True)
		program.add_argument('--gitlab-auth', required=True)
	args = program.parse_known_args()[0]


def run():
	host = args.gitlab_host
	slugs = args.gitlab_slug
	auth = args.gitlab_auth
	result = []

	for slug in slugs:
		result.extend(fetch(host, slug, auth))
	return result


def fetch(host, slug, auth):
	response = None

	if host and slug and auth:
		response = requests.get(host + '/api/v4/projects/' + slug + '/pipelines', headers =
		{
			'Private-Token': auth
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()
		pipeline = str(data[0]['id'])

		if pipeline:
			return fetch_jobs(host, slug, pipeline, auth)
	return []


def fetch_jobs(host, slug, pipeline, auth):
	response = None

	if host and slug and pipeline and auth:
		response = requests.get(host + '/api/v4/projects/' + slug + '/pipelines/' + pipeline + '/jobs', headers =
		{
			'Private-Token': auth
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
