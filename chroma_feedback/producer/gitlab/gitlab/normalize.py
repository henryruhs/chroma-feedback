from chroma_feedback import helper
from chroma_feedback.typing import Producer, Status


def normalize_data(slug : str, url: str, status : str) -> Producer:
	return\
	{
		'name': 'gitlab',
		'slug': slug,
		'url': url,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> Status:
	status = helper.to_lower_case(status)

	if status == 'skipped':
		return 'skipped'
	if status in ['created', 'running', 'pending']:
		return 'started'
	if status == 'canceled':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
