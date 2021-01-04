from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'codeship',
		'slug': build['slug'],
		'active': True,
		'status': normalize_status(build['status'])
	}


def normalize_status(status : str) -> str:
	status = helper.to_lower_case(status)

	if status in ['initiated', 'testing', 'waiting']:
		return 'started'
	if status in ['error', 'blocked', 'ignored']:
		return 'errored'
	if status in ['failed', 'infrastructure_failure']:
		return 'failed'
	return 'passed'
