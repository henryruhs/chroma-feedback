import requests


def fetch_data(host, slug):
	response = requests.get(host + '/job/' + slug + '/api/json')
	if response.status_code == 200:
		data = response.json()
		return normalize_data(data)
	return []


def normalize_data(project):
	return\
	[
		{
			'provider': 'jenkins',
			'slug': project['displayName'],
			'active': True,
			'status': normalize_status(project)
		}
	]


def normalize_status(project):
	if 'anime' in project['color']:
		return 'process'
	if project['color'] == 'grey':
		return 'errored'
	if project['color'] == 'red':
		return 'failed'
	return 'passed'
