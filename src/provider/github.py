import base64
import requests


def fetch(host, slug, auth):
	response = None
	if host is None:
		host = 'https://api.github.com'
	if slug and auth:
		response = requests.get(host + '/repos/' + slug + '/status/master', headers =
		{
			'Authorization': 'Basic ' + base64.b64encode(auth.encode('utf-8')).decode('ascii')
		})

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
	if status == 'failure':
		return 'failed'
	return 'passed'
