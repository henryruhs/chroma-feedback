from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'circle',
		'slug': build['project_slug'] + '/' + build['name'],
		'active': True,
		'status': normalize_status(build['status'])
	}


def normalize_status(status : str) -> str:
	status = helper.to_lower_case(status)

	if status in ['queued', 'running', 'scheduled']:
		return 'started'
	if status in ['canceled', 'no_tests']:
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
