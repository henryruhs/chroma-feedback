from chroma_feedback import helper
from chroma_feedback.typing import Producer, Status


def normalize_data(slug : str, url : str, status : str) -> Producer:
	return\
	{
		'name': 'netlify',
		'slug': slug,
		'url': url,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> Status:
	status = helper.to_lower_case(status)

	if status == 'error':
		return 'failed'
	return 'passed'
