import base64
import requests


def fetch(host, slug, token):
	response = None
	headers = None
	if host is None:
		host = 'https://teamcity.jetbrains.com'
	if token:
		headers =\
		{
			'Accept': 'application/json',
			'Authorization': 'Basic ' + base64.b64encode(token.encode('utf-8')).decode('ascii')
		}
	if host and token:
		if slug:
			response = requests.get(host + '/app/rest/buildTypes?locator=affectedProject:(id:' + slug + ')&fields=buildType(builds($locator(running:any),build(id,running,status,buildType(id,projectName))))', headers = headers)
		else:
			response = requests.get(host + '/app/rest/buildTypes/?fields=buildType(builds($locator(user:current,running:any),build(id,running,status,buildType(id,projectName))))', headers = headers)

	# process response

	if response and response.status_code == 200:
		data = response.json()
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