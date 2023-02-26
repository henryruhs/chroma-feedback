from chroma_feedback import helper
from chroma_feedback.typing import Producer, Status


def normalize_data(slug : str, status : str, is_active : bool) -> Producer:
	return\
	{
		'name': 'travis',
		'slug': slug,
		'url': None,
		'status': normalize_status(status, is_active)
	}


def normalize_status(status : str, is_active : bool) -> Status:
	status = helper.to_lower_case(status)

	if not is_active:
		return 'skipped'
	if status in ['created', 'started']:
		return 'started'
	if status in ['cancelled', 'errored']:
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
