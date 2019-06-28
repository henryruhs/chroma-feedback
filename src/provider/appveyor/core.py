import requests
from .normalize import normalize_data


def fetch(host, slug, auth):
	response = None

	if host is None:
		host = 'https://ci.appveyor.com'
	if slug:
		response = requests.get(host + '/api/projects/' + slug)
	if auth:
		response = requests.get(host + '/api/projects', headers =
		{
			'Authorization': 'Bearer ' + auth
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
