from chroma_feedback import helper
from chroma_feedback.typing import StatusType, ProducerModel


def normalize_data(slug : str, status : str) -> ProducerModel:
	return\
	{
		'producer': 'codeship',
		'slug': slug,
		'active': True,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> StatusType:
	status = helper.to_lower_case(status)

	if status in ['initiated', 'testing', 'waiting']:
		return 'started'
	if status in ['error', 'blocked', 'ignored']:
		return 'errored'
	if status in ['failed', 'infrastructure_failure']:
		return 'failed'
	return 'passed'
