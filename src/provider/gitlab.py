import requests


def fetch(host, slug, token):
	response = None
	if host is None:
		host = 'https://gitlab.com'
	if slug and token:
		response = requests.get(host + '/api/v4/projects/' + slug + '/jobs', headers =
		{
			'Private-Token': token
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()
		result = []
		for project in data:
			result.extend(normalize_data(project))
		return result
	return []


def normalize_data(project):
	return\
	[
		{
			'provider': 'gitlab',
			'slug': project['user']['username'] + '/' + project['name'],
			'active': True,
			'status': normalize_status(project['status'])
		}
	]


def normalize_status(status):
	if status == 'created' or status == 'running' or status == 'pending':
		return 'process'
	if status == 'canceled' or status == 'skipped':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
