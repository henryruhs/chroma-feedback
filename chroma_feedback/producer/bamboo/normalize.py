from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'bamboo',
		'slug': build['key'],
		'active': True,
		'status': normalize_status(build['buildState'])
	}


def normalize_status(status : str) -> str:
	status = helper.to_lower_case(status)

	if status == 'failed':
		return 'failed'
	return 'passed'


def normalize_slug(slug : str) -> str:
	if '-' in slug:
		return slug + '-latest'
	return slug
