from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'bamboo',
		'slug': project['key'],
		'active': True,
		'status': normalize_status(project['buildState'])
	}


def normalize_status(status : str) -> str:
	status = helper.to_lower_case(status)

	if status == 'failed':
		return 'failed'
	return 'passed'
