from typing import Any, Dict


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'wercker',
		'slug': project['slug'],
		'active': True,
		'status': normalize_status(project['status'], project['result'])
	}


def normalize_status(status : str, result : str) -> str:
	if status == 'running':
		return 'process'
	if result == 'aborted':
		return 'errored'
	if result == 'failed':
		return 'failed'
	return 'passed'
