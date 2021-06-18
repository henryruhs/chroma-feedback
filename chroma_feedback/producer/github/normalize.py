from chroma_feedback import helper
from chroma_feedback.typing import StatusType, ProducerModel


def normalize_data(slug : str, status : str, result : str) -> ProducerModel:
	return\
	{
		'producer': 'github',
		'slug': slug,
		'active': True,
		'status': normalize_status(status, result)
	}


def normalize_status(status : str, result : str) -> StatusType:
	status = helper.to_lower_case(status)
	result = helper.to_lower_case(result)

	if status in ['in_progress', 'queued']:
		return 'started'
	if result in ['cancelled', 'timed_out']:
		return 'errored'
	if result == 'failure':
		return 'failed'
	return 'passed'
