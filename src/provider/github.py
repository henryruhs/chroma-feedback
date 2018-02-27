import requests


def fetch(host, slug):
	response = None
	if host is None:
		host = 'https://api.github.com'
	if slug:
		response = requests.get(host + '/repos/' + slug + '/status/master')

	# process response

	if response and response.status_code == 200:
		data = response.json()
		if data:
			return normalize_data(data)
	return []


def normalize_data(project):
	return\
	[
		{
			'provider': 'github',
			'slug': project['repository']['full_name'],
			'active': True,
			'status': normalize_status(project['state'])
		}
	]


def normalize_status(status):
	if status == 'pending':
		return 'process'
	if status == 'error':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
