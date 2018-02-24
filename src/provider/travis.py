import requests


def fetch(slug):
	response = requests.get('https://api.travis-ci.org/repos/' + slug, headers =
	{
		'Accept': 'application/vnd.travis-ci.2+json'
	})

	# process response

	if response.status_code == 200:
		data = response.json()
		if 'repo' in data:
			return normalize_data(data['repo'])
		if 'repos' in data:
			result = []
			for project in data['repos']:
				result.extend(normalize_data(project))
			return result
	return []


def normalize_data(project):
	return\
	[
		{
			'provider': 'travis',
			'slug': project['slug'],
			'active': project['active'],
			'status': normalize_status(project)
		}
	]


def normalize_status(project):
	if project['last_build_finished_at'] is None:
		return 'process'
	return project['last_build_state']
