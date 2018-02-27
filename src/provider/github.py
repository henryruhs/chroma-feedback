import requests


def fetch(host, slug):
	response = None
	if host is None:
		host = 'https://api.github.com'
	if slug:
		reference = fetch_reference(host, slug)
		response = requests.get(host + '/repos/' + slug + '/status/' + reference)

	# process response

	if response and response.status_code == 200:
		data = response.json()
		if data:
			return normalize_data(data)
	return []


def fetch_reference(host, slug):
	response = requests.get(host + '/repos/' + slug + '/git/refs')
	if response and response.status_code == 200:
		data = response.json()
		if 'object' in data[0]:
			return data[0]['object']['sha']
	return 'master'


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
	if status == 'failure':
		return 'failed'
	return 'passed'
