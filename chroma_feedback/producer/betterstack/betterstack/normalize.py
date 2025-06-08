from chroma_feedback.types import Producer, Status


def normalize_data(slug : str, url : str, status : str) -> Producer:
	return\
	{
		'name': 'betterstack',
		'slug': slug,
		'url': url,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> Status:
	if status in [ 'paused', 'maintenance' ]:
		return 'skipped'
	if status in [ 'pending', 'validating' ]:
		return 'started'
	if status == 'down':
		return 'failed'
	return 'passed'
