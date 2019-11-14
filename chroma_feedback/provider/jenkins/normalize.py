from typing import Any, Dict


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'provider': 'jenkins',
		'slug': project['displayName'],
		'active': True,
		'status': normalize_status(project['color'])
	}


def normalize_status(color : str) -> str:
	if 'anime' in color:
		return 'process'
	if color == 'grey':
		return 'errored'
	if color == 'red':
		return 'failed'
	return 'passed'
