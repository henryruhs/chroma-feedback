def normalize_data(build):
	return\
	[
		{
			'provider': 'codeship',
			'slug': str(build['project_id']),
			'active': True,
			'status': normalize_status(build['status'])
		}
	]


def normalize_status(status):
	if status in ['initiated', 'testing', 'waiting']:
		return 'process'
	if status in ['error', 'blocked', 'ignored']:
		return 'errored'
	if status in ['failed', 'infrastructure_failure']:
		return 'failed'
	return 'passed'
