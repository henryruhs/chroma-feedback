import requests


def fetch_data(host, slug):
	response = requests.get(host + '/job/' + slug + '/api/json')
	if response.status_code == 200:
		data = response.json()
		return normalize_data(data)
	return []


def normalize_data(data):
	return\
	[
		{
			'provider': 'Jenkins',
			'slug': data['displayName'],
			'active': True,
			'status': normalize_status(data)
		}
	]


def normalize_status(data):
	if data['color'] == 'red':
		return 'failed'
	return 'passed'

