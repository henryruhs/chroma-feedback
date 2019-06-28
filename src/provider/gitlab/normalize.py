def normalize_data(project):
	return\
	[
		{
			'provider': 'gitlab',
			'slug': project['user']['username'] + '/' + project['slug'] + '/' + project['name'],
			'active': True,
			'status': normalize_status(project['status'])
		}
	]


def normalize_status(status):
	if status == 'created' or status == 'running' or status == 'pending':
		return 'process'
	if status == 'canceled' or status == 'skipped':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
