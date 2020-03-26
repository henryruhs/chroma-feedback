from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'teamcity',
		'slug': build['buildType']['projectName'],
		'active': True,
		'status': normalize_status(build['running'], build['status'])
	}


def normalize_status(running : str, status : str) -> str:
	status = helper.to_lower_case(status)

	if running is True:
		return 'process'
	if status == 'error':
		return 'errored'
	if status == 'failure':
		return 'failed'
	return 'passed'
