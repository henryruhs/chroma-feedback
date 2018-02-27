import requests


def fetch(host, slug, token):
	response = None
	if host is None:
		host = 'https://ci.appveyor.com'
	if slug:
		response = requests.get(host + '/api/projects/' + slug)
	if token:
		response = requests.get(host + '/api/projects', headers =
		{
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
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
			'status': normalize_status(build['status'])
		}
	]


def normalize_status(status):
	if status == 'queued' or status == 'running':
		return 'process'
	if status == 'canceled':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
