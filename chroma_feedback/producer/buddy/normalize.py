from chroma_feedback import helper
from chroma_feedback.typing import Status, Producer


def normalize_data(slug : str, status : str) -> Producer:
	return\
	{
		'producer': 'buddy',
		'slug': slug,
		'active': True,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> Status:
	status = helper.to_lower_case(status)

	if status == 'inprogress':
		return 'started'
	if status == 'failed':
		return 'failed'
	return 'passed'
