from typing import Any, Dict


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'provider': 'bamboo',
		'slug': project['key'],
		'active': True,
		'status': normalize_status(project['buildState'].lower(), project['lifeCycleState'].lower())
	}


def normalize_status(status : str, lifecycle : str) -> str:
	if lifecycle == 'inprogress':
		return 'process'
	if status == 'failed':
		return 'failed'
	return 'passed'
