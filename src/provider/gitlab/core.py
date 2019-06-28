import requests
from .normalize import normalize_data


def fetch(host, slug, auth):
	response = None
	if host is None:
		host = 'https://gitlab.com'
	if slug and auth:
		response = requests.get(host + '/api/v4/projects/' + slug + '/pipelines', headers =
		{
			'Private-Token': auth
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()
		pipeline = str(data[0]['id'])
		if pipeline:
			return fetch_jobs(host, slug, pipeline, auth)
	return []


def fetch_jobs(host, slug, pipeline, auth):
	response = None
	if host and slug and pipeline and auth:
		response = requests.get(host + '/api/v4/projects/' + slug + '/pipelines/' + pipeline + '/jobs', headers =
		{
			'Private-Token': auth
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()
		result = []
		for project in data:
			project['slug'] = slug
			result.extend(normalize_data(project))
		return result
	return []
