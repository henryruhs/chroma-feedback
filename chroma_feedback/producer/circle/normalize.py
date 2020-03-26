from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'circle',
		'slug': project['username'] + '/' + project['reponame'],
		'active': True,
		'status': normalize_status(project['status'])
	}


def normalize_status(status : str) -> str:
	status = helper.to_lower_case(status)

	if status in ['queued', 'running', 'scheduled']:
		return 'process'
	if status in ['canceled', 'no_tests']:
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
