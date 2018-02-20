import requests


def mine_data(args):
	data = []
	for provider in args.provider:
		for slug in args.slug:
			data.extend(fetch_data(provider, slug))
	return data


def fetch_data(provider, slug):
	if provider == 'appveyor':
		return fetch_appveyor(slug)
	if provider == 'travis':
		return fetch_travis(slug)
	return []


def fetch_appveyor(slug):
	data = requests.get('https://ci.appveyor.com/api/projects/' + slug, headers =
	{
		'Accept': 'application/json'
	}).json()

	# handle data

	if 'build' in data:
		return normalize_appveyor(data['build'])
	return []


def normalize_appveyor(data):
	return\
	{
		'active': True,
		'process': data['finished'] is None,
		'status': data['status']
	}


def fetch_travis(slug):
	data = requests.get('https://api.travis-ci.org/repos/' + slug, headers =
	{
		'Accept': 'application/vnd.travis-ci.2+json'
	}).json()

	# handle data

	if 'repos' in data:
		result = []
		for repo in data['repos']:
			result.extend(normalize_travis(repo))
		return result
	if 'repo' in data:
		return normalize_travis(data['repo'])
	return []


def normalize_travis(data):
	return\
	{
		'active': data['active'],
		'process': data['last_build_finished_at'] is None,
		'status': data['last_build_state']
	}
