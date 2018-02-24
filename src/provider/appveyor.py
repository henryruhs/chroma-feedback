import requests


def fetch(slug, token):
	if slug:
		response = requests.get('https://ci.appveyor.com/api/projects/' + slug)
	if token:
		response = requests.get('https://ci.appveyor.com/api/projects', headers =
		{
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response.status_code == 200:
		data = response.json()
		if 'project' and 'build' in data:
			return normalize_data(data['project'], data['build'])
		if 'builds' in data[0]:
			result = []
			for project in data:
				if project['builds']:
					result.extend(normalize_data(project, project['builds'][0]))
			return result
	return []


def normalize_data(project, build):
	return\
	[
		{
			'provider': 'appveyor',
			'slug': project['accountName'] + '/' + project['slug'],
			'active': True,
			'status': normalize_status(build)
		}
	]


def normalize_status(build):
	if build['status'] == 'running':
		return 'process'
	if build['status'] == 'success':
		return 'passed'
	return build['status']
