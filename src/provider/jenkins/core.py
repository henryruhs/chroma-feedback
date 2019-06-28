import requests
from .normalize import normalize_data


def fetch(host, slug, auth):
	response = None
	if host and slug:
		response = requests.get(host + '/job/' + slug + '/api/json')

	# process response

	if response and response.status_code == 200:
		data = response.json()
		if data:
			return normalize_data(data)
	return []
