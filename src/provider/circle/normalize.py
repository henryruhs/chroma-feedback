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
	if status == 'queued' or status == 'running' or status == 'scheduled':
		return 'process'
	if status == 'canceled' or status == 'no_tests':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
