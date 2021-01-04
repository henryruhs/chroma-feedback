from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'jenkins',
		'slug': project['slug'],
		'active': True,
		'status': normalize_status(project['result'], project['building'])
	}


def normalize_status(status : str, process : bool) -> str:
	status = helper.to_lower_case(status)

	if process is True:
		return 'process'
	if status in ['unstable', 'not_build']:
		return 'errored'
	if status == 'failure':
		return 'failed'
	return 'passed'
