from typing import Any, Dict


def normalize_data(project : Dict[str, Any], build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'provider': 'appveyor',
		'slug': project['accountName'] + '/' + project['slug'],
		'active': True,
		'status': normalize_status(build['status'])
	}


def normalize_status(status : str) -> str:
	if status in ['queued', 'running']:
		return 'process'
	if status == 'canceled':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
