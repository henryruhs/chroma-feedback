from chroma_feedback import helper
from chroma_feedback.typing import StatusType, ProducerModel


def normalize_data(slug : str, status : str) -> ProducerModel:
	return\
	{
		'producer': 'circle',
		'slug': slug,
		'active': True,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> StatusType:
	status = helper.to_lower_case(status)

	if status in ['queued', 'running', 'scheduled']:
		return 'started'
	if status in ['canceled', 'no_tests']:
		return 'errored'
	if status in ['failed', 'failing']:
		return 'failed'
	return 'passed'
