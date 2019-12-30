from typing import Any, Dict


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'wercker',
		'slug': project['slug'],
		'active': True,
		'status': normalize_status(project['status'])
	}


def normalize_status(status : str) -> str:
	if status == 'aborted':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
