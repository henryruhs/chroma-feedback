def normalize_data(project, build):
	return\
	[
		{
			'provider': 'appveyor',
			'slug': project['accountName'] + '/' + project['slug'],
			'active': True,
			'status': normalize_status(build['status'])
		}
	]


def normalize_status(status):
	if status == 'queued' or status == 'running':
		return 'process'
	if status == 'canceled':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
