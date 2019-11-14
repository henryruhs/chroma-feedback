from typing import Any, Dict


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'provider': 'github',
		'slug': project['repository']['full_name'],
		'active': True,
		'status': normalize_status(project['state'])
	}


def normalize_status(status : str) -> str:
	if status == 'pending':
		return 'process'
	if status == 'error':
		return 'errored'
	if status == 'failure':
		return 'failed'
	return 'passed'
