def normalize_data(project):
	return\
	[
		{
			'provider': 'jenkins',
			'slug': project['displayName'],
			'active': True,
			'status': normalize_status(project['color'])
		}
	]


def normalize_status(color):
	if 'anime' in color:
		return 'process'
	if color == 'grey':
		return 'errored'
	if color == 'red':
		return 'failed'
	return 'passed'
