from chroma_feedback import helper
from chroma_feedback.typing import StatusType, ProducerModel


def normalize_data(slug : str, status : str) -> ProducerModel:
	return\
	{
		'producer': 'bitbucket',
		'slug': slug,
		'active': True,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> StatusType:
	status = helper.to_lower_case(status)

	if status == 'inprogress':
		return 'started'
	if status == 'stopped':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
