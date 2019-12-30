from typing import Any, Dict


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'gitlab',
		'slug': build['slug'] + '/' + build['name'],
		'active': True,
		'status': normalize_status(build['status'].lower())
	}


def normalize_status(status : str) -> str:
	if status in ['created', 'running', 'pending']:
		return 'process'
	if status in ['canceled', 'skipped']:
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
