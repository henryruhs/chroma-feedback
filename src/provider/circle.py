import base64
import requests


def fetch(host, slug, auth):
	response = None
	if host is None:
		host = 'https://circleci.com'
	if slug:
		response = requests.get(host + '/api/v1.1/project/' + slug)
	if auth:
		response = requests.get(host + '/api/v1.1/recent-builds', headers =
		{
			'Authorization': 'Basic ' + base64.b64encode(auth.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()
		for project in data:
			return normalize_data(project)
	return []


def normalize_data(project):
	return\
	[
		{
			'provider': 'circle',
			'slug': project['username'] + '/' + project['reponame'],
			'active': True,
			'status': normalize_status(project['status'])
		}
	]


def normalize_status(status):
	if status == 'queued' or status == 'running' or status == 'scheduled':
		return 'process'
	if status == 'canceled' or status == 'no_tests':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
