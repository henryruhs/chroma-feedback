import base64
import requests

from .normalize import normalize_data


def fetch(host, slug, auth):
	response = None
	if host is None:
		host = 'https://api.github.com'
	if slug and auth:
		response = requests.get(host + '/repos/' + slug + '/status/master', headers =
		{
			'Authorization': 'Basic ' + base64.b64encode(auth.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()
		if data:
			return normalize_data(data)
	return []
