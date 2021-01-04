from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'bitbucket',
		'slug': build['repository']['full_name'],
		'active': True,
		'status': normalize_status(build['state']['result']['name'])
	}


def normalize_status(status : str) -> str:
	status = helper.to_lower_case(status)

	if status == 'inprogress':
		return 'started'
	if status == 'stopped':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
