def normalize_data(build):
	return\
	[
		{
			'provider': 'codeship',
			'slug': build['project_id'],
			'active': True,
			'status': normalize_status(build['status'])
		}
	]


def normalize_status(status):
	if status in ['initiated', 'waiting']:
		return 'process'
	if status in ['error', 'blocked', 'ignored']:
		return 'errored'
	if status in ['failed', 'infrastructure_failure']:
		return 'failed'
	return 'passed'

