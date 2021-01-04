from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(project : Dict[str, Any], build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'appveyor',
		'slug': project['accountName'] + '/' + project['slug'],
		'active': True,
		'status': normalize_status(build['status'])
	}


def normalize_status(status : str) -> str:
	status = helper.to_lower_case(status)

	if status in ['queued', 'running']:
		return 'started'
	if status == 'canceled':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
