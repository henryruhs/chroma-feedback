def normalize_data(project):
	return\
	[
		{
			'provider': 'travis',
			'slug': project['slug'],
			'active': project['active'] is True,
			'status': normalize_status(project['last_build_state'])
		}
	]


def normalize_status(status):
	if status == 'created' or status == 'started':
		return 'process'
	if status == 'cancelled' or status == 'errored':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
