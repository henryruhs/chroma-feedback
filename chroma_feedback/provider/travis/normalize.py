from typing import Any, Dict


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'provider': 'travis',
		'slug': project['slug'],
		'active': project['active'],
		'status': normalize_status(project['last_build_state'])
	}


def normalize_status(status : str) -> str:
	if status in ['created', 'started']:
		return 'process'
	if status in ['cancelled', 'errored']:
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
