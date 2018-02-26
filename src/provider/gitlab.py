import requests


def fetch(host, slug, token):
	response = None
	if slug:
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
			'status': normalize_status(project)
		}
	]


def normalize_status(project):
	if project['status'] == 'running' or project['status'] == 'pending':
		return 'process'
	if project['status'] == 'success':
		return 'passed'
	return project['status']
