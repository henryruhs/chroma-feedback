from chroma_feedback import helper
from chroma_feedback.typing import Status, Producer


def normalize_data(slug : str, active : bool, status : str) -> Producer:
	return\
	{
		'producer': 'travis',
		'slug': slug,
		'active': active,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> Status:
	status = helper.to_lower_case(status)

	if status in ['created', 'started']:
		return 'started'
	if status in ['cancelled', 'errored']:
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
