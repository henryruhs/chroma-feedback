from chroma_feedback import helper
from chroma_feedback.typing import StatusType, ProducerModel


def normalize_data(slug : str, result : str, is_building : bool) -> ProducerModel:
	return\
	{
		'producer': 'jenkins',
		'slug': slug,
		'active': True,
		'status': normalize_status(result, is_building)
	}


def normalize_status(result : str, is_building: bool) -> StatusType:
	result = helper.to_lower_case(result)

	if is_building is True:
		return 'started'
	if result in ['unstable', 'not_build']:
		return 'errored'
	if result == 'failure':
		return 'failed'
	return 'passed'
