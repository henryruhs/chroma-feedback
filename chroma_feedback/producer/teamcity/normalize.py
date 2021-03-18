from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(slug : str, status : str, is_running : bool) -> Dict[str, Any]:
	return\
	{
		'producer': 'teamcity',
		'slug': slug,
		'active': True,
		'status': normalize_status(status, is_running)
	}


def normalize_status(status : str, is_running : bool) -> str:
	status = helper.to_lower_case(status)

	if is_running is True:
		return 'started'
	if status == 'error':
		return 'errored'
	if status == 'failure':
		return 'failed'
	return 'passed'
