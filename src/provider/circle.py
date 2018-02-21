import requests


def fetch_data(slug):
	response = requests.get('https://circleci.com/api/v1.1/project/' + slug)
	if response.status_code == 200:
		data = response.json()
		return normalize_data(data[0])
	return []


def normalize_data(data):
	return\
	[
		{
			'provider': 'Circle CI',
			'slug': data['username'] + '/' + data['reponame'],
			'active': True,
			'status': normalize_status(data)
		}
	]


def normalize_status(data):
	if data['lifecycle'] == 'running':
		return 'process'
	if data['status'] == 'fixed':
		return 'passed'
	return data['status']
