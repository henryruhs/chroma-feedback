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
	if status in ['created', 'running', 'pending']:
		return 'process'
	if status in ['canceled', 'skipped']:
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
