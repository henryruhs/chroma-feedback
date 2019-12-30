from typing import Any, Dict


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'wercker',
		'slug': build['slug'],
		'active': True,
		'status': normalize_status(build['status'].lower(), build['result'].lower())
	}


def normalize_status(status : str, result : str) -> str:
	if status == 'running':
		return 'process'
	if result == 'aborted':
		return 'errored'
	if result == 'failed':
		return 'failed'
	return 'passed'
