from typing import Any, Dict


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'bamboo',
		'slug': project['key'],
		'active': True,
		'status': normalize_status(project['buildState'].lower())
	}


def normalize_status(status : str) -> str:
	if status == 'failed':
		return 'failed'
	return 'passed'
