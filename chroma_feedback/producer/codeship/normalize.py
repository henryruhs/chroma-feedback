from chroma_feedback import helper
from chroma_feedback.typing import Status, Producer


def normalize_data(slug : str, status : str) -> Producer:
	return\
	{
		'producer': 'codeship',
		'slug': slug,
		'active': True,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> Status:
	status = helper.to_lower_case(status)

	if status in ['initiated', 'testing', 'waiting']:
		return 'started'
	if status in ['error', 'blocked', 'ignored']:
		return 'errored'
	if status in ['failed', 'infrastructure_failure']:
		return 'failed'
	return 'passed'
