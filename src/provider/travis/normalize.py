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
	if status in ['created', 'started']:
		return 'process'
	if status in ['cancelled', 'errored']:
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
