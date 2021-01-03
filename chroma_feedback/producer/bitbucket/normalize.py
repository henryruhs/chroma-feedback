from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(data : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'bitbucket',
		'slug': data['repository']['full_name'],
		'active': True,
		'status': normalize_status(data['state']['result']['name'])
	}


def normalize_status(status : str) -> str:
	status = helper.to_lower_case(status)

	if status == 'inprogress':
		return 'process'
	if status == 'stopped':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
