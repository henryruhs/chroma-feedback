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
