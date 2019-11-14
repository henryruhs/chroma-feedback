from typing import Any, Dict


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'provider': 'gitlab',
		'slug': project['slug'] + '/' + project['name'],
		'active': True,
		'status': normalize_status(project['status'])
	}


def normalize_status(status : str) -> str:
	if status in ['created', 'running', 'pending']:
		return 'process'
	if status in ['canceled', 'skipped']:
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
