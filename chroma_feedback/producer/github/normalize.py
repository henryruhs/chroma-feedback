from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'github',
		'slug': build['repository']['full_name'],
		'active': True,
		'status': normalize_status(build['conclusion'])
	}


def normalize_status(status : str) -> str:
	status = helper.to_lower_case(status)

	if status == 'pending':
		return 'process'
	if status == 'error':
		return 'errored'
	if status == 'failure':
		return 'failed'
	return 'passed'
