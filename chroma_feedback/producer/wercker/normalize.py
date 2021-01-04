from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'wercker',
		'slug': build['slug'],
		'active': True,
		'status': normalize_status(build['status'], build['result'])
	}


def normalize_status(status : str, result : str) -> str:
	status = helper.to_lower_case(status)
	result = helper.to_lower_case(result)

	if status == 'running':
		return 'started'
	if result == 'aborted':
		return 'errored'
	if result == 'failed':
		return 'failed'
	return 'passed'
