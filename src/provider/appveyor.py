import requests


def fetch_data(slug):
	response = requests.get('https://ci.appveyor.com/api/projects/' + slug)
	if response.status_code == 200:
		data = response.json()
		if 'project' and 'build' in data:
			return normalize_data(data)
	return []


def normalize_data(data):
	return\
	[
		{
			'provider': 'AppVeyor',
			'slug': data['project']['accountName'] + '/' + data['project']['slug'],
			'active': True,
			'status': normalize_status(data)
		}
	]


def normalize_status(data):
	if data['build']['finished'] is None:
		return 'process'
	if data['build']['status'] == 'success':
		return 'passed'
	return data['build']['status']
