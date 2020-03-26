from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'jenkins',
		'slug': project['slug'],
		'active': True,
		'status': normalize_status(project['building'], project['result'])
	}


def normalize_status(building : bool, status : str) -> str:
	status = helper.to_lower_case(status)

	if building is True:
		return 'process'
	if status == 'unstable':
		return 'errored'
	if status in ['failure', 'not_build']:
		return 'failed'
	return 'passed'
