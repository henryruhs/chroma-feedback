import requests


def fetch_data(slug, token):
	if slug:
		response = requests.get('https://ci.appveyor.com/api/projects/' + slug)
	if token:
		response = requests.get('https://ci.appveyor.com/api/projects', headers =
		{
			'Authorization': 'Bearer ' + token
		})
	if response.status_code == 200:
		data = response.json()
		if 'project' and 'build' in data:
			return normalize_data(data['project'], data['build'])
		result = []
		for project in data:
			result.extend(normalize_data(project, project['builds'][0]))
		return result
	return []


def normalize_data(project, build):
	return\
	[
		{
			'provider': 'AppVeyor',
			'slug': project['accountName'] + '/' + project['slug'],
			'active': True,
			'status': normalize_status(build)
		}
	]


def normalize_status(build):
	if build['finished'] is None:
		return 'process'
	if build['status'] == 'success':
		return 'passed'
	return build['status']
