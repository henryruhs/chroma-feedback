from typing import Any, Dict
from chroma_feedback import helper


def normalize_data(build : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'github',
		'slug': build['repository']['full_name'],
		'active': True,
		'status': normalize_status(build['status'], build['conclusion'])
	}


def normalize_status(status : str, conclusion : str) -> str:
	status = helper.to_lower_case(status)

	if status in ['in_progress', 'queued']:
		return 'started'
	if conclusion in ['cancelled', 'timed_out']:
		return 'errored'
	if conclusion == 'failure':
		return 'failed'
	return 'passed'
