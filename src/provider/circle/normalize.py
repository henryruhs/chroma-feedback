def normalize_data(project):
	return\
	[
		{
			'provider': 'circle',
			'slug': project['username'] + '/' + project['reponame'],
			'active': True,
			'status': normalize_status(project['status'])
		}
	]


def normalize_status(status):
	if status in ['queued', 'running', 'scheduled']:
		return 'process'
	if status in ['canceled', 'no_tests']:
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
