from chroma_feedback import helper
from chroma_feedback.typing import Producer, Status


def normalize_data(slug : str, result : str, is_building : bool) -> Producer:
	return\
	{
		'name': 'jenkins',
		'slug': slug,
		'url': None,
		'status': normalize_status(result, is_building)
	}


def normalize_status(result : str, is_building: bool) -> Status:
	result = helper.to_lower_case(result)

	if is_building:
		return 'started'
	if result in ['unstable', 'not_build']:
		return 'errored'
	if result == 'failure':
		return 'failed'
	return 'passed'
