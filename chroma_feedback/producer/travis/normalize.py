from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'travis',
		'slug': project['slug'],
		'active': project['active'],
		'status': normalize_status(project['last_build_state'])
	}


def normalize_status(status : str) -> str:
	status = helper.to_lower_case(status)

	if status in ['created', 'started']:
		return 'started'
	if status in ['cancelled', 'errored']:
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'
