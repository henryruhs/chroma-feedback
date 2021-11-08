from chroma_feedback import helper
from chroma_feedback.typing import Status, Producer


def normalize_data(slug : str, status : str, result : str) -> Producer:
	return\
	{
		'producer': 'wercker',
		'slug': slug,
		'active': True,
		'status': normalize_status(status, result)
	}


def normalize_status(status : str, result : str) -> Status:
	status = helper.to_lower_case(status)
	result = helper.to_lower_case(result)

	if status == 'running':
		return 'started'
	if result == 'aborted':
		return 'errored'
	if result == 'failed':
		return 'failed'
	return 'passed'
