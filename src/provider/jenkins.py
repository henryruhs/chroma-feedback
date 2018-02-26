import requests


def fetch(host, slug):
	response = None
	if host and slug:
		try:
			response = requests.get(host + '/job/' + slug + '/api/json')
		except requests.exceptions.ConnectionError:
			pass

	# process response

	if response and response.status_code == 200:
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
			'status': normalize_status(project['color'])
		}
	]


def normalize_status(color):
	if 'anime' in color:
		return 'process'
	if color == 'grey':
		return 'errored'
	if color == 'red':
		return 'failed'
	return 'passed'
