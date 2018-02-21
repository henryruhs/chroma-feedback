import requests


def fetch_data(slug):
	response = requests.get('https://api.travis-ci.org/repos/' + slug, headers =
	{
		'Accept': 'application/vnd.travis-ci.2+json'
	})
	if response.status_code == 200:
		data = response.json()
		if 'repos' in data:
			result = []
			for repo in data['repos']:
				result.extend(normalize_data(repo))
			return result
		if 'repo' in data:
			return normalize_data(data['repo'])
	return []


def normalize_data(data):
	return \
	[
		{
			'provider': 'Travis CI',
			'slug': data['slug'],
			'active': data['active'],
			'status': normalize_status(data)
		}
	]


def normalize_status(data):
	if data['last_build_finished_at'] is None:
		return 'process'
	return data['last_build_state']
