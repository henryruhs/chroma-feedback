import base64
import requests

from .normalize import normalize_data


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
