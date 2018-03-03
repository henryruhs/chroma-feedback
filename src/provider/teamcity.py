import base64
import requests


def fetch(host, slug, token):
	response = None
	if host and slug and token:
		response = requests.get(host + '/httpAuth/app/rest/buildTypes/id:' + slug + '/builds?fields=build(id,running,status,buildType(id,projectName))', headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Basic ' + base64.b64encode(token.encode('utf-8')).decode('ascii')
		})
	elif host and token:
		response = requests.get(host + '/httpAuth/app/rest/buildTypes/?fields=buildType(builds($locator(user:current),build(id,running,status,buildType(id,projectName))))', headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Basic ' + base64.b64encode(token.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()
		if 'build' in data:
			return normalize_data(data['build'][0])
		if 'buildType' in data:
			result = []
			for project in data['buildType']:
				if project['builds']['build']:
					result.extend(normalize_data(project['builds']['build'][0]))
			return result
	return []


def normalize_data(build):
	return\
	[
		{
			'provider': 'teamcity',
			'slug': build['buildType']['projectName'],
			'active': True,
			'status': normalize_status(build['running'], build['status'].lower())
		}
	]


def normalize_status(running, status):
	if running is True:
		return 'process'
	if status == 'error':
		return 'errored'
	if status == 'failure':
		return 'failed'
	return 'passed'
