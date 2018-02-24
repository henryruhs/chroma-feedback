import requests


def fetch(slug, token):
	if slug:
		response = requests.get('https://circleci.com/api/v1.1/project/' + slug)
	if token:
		response = requests.get('https://circleci.com/api/v1.1/recent-builds?circle-token=' + token)

	# process response

	if response.status_code == 200:
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
			'status': normalize_status(project)
		}
	]


def normalize_status(project):
	if project['lifecycle'] == 'running':
		return 'process'
	if project['status'] == 'success' or project['status'] == 'fixed':
		return 'passed'
	if project['status'] == 'no_tests':
		return 'errored'
	return project['status']
