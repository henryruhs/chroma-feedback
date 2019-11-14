from typing import Any, Dict


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'provider': 'teamcity',
		'slug': build['buildType']['projectName'],
		'active': True,
		'status': normalize_status(build['running'], build['status'].lower())
	}


def normalize_status(running : str, status : str) -> str:
	if running is True:
		return 'process'
	if status == 'error':
		return 'errored'
	if status == 'failure':
		return 'failed'
	return 'passed'
