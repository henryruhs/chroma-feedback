from chroma_feedback import helper
from chroma_feedback.typing import StatusType, ProducerModel


def normalize_data(slug : str, paused : bool, status : str, is_running : bool) -> ProducerModel:
	return\
	{
		'producer': 'teamcity',
		'slug': slug,
		'active': paused is False,
		'status': normalize_status(status, is_running)
	}


def normalize_status(status : str, is_running : bool) -> StatusType:
	status = helper.to_lower_case(status)

	if is_running is True:
		return 'started'
	if status == 'error':
		return 'errored'
	if status == 'failure':
		return 'failed'
	return 'passed'
