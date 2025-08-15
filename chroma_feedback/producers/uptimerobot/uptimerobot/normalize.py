from chroma_feedback.types import Producer, Status


def normalize_data(slug : str, url : str, status : int) -> Producer:
	return\
	{
		'name': 'uptimerobot',
		'slug': slug,
		'url': url,
		'status': normalize_status(status)
	}


def normalize_status(status : int) -> Status:
	if status == 0:
		return 'skipped'
	if status == 1:
		return 'started'
	if status == 9:
		return 'failed'
	return 'passed'
