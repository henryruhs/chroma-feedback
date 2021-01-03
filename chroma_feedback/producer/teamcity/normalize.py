from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'teamcity',
		'slug': build['buildType']['projectName'],
		'active': True,
		'status': normalize_status(build['status'], build['running'])
	}


def normalize_status(status : str, process : str) -> str:
	status = helper.to_lower_case(status)

	if process is True:
		return 'process'
	if status == 'error':
		return 'errored'
	if status == 'failure':
		return 'failed'
	return 'passed'
