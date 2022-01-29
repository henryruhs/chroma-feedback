from chroma_feedback import helper
from chroma_feedback.typing import Status, Producer


def normalize_data(slug : str, url : str, status : str, conclusion : str) -> Producer:
	return\
	{
		'producer': 'github',
		'slug': slug,
		'url': url,
		'status': normalize_status(status, conclusion)
	}


def normalize_status(status : str, conclusion : str) -> Status:
	status = helper.to_lower_case(status)
	conclusion = helper.to_lower_case(conclusion)

	if conclusion in ['skipped', 'stale']:
		return 'skipped'
	if status in ['in_progress', 'queued']:
		return 'started'
	if conclusion in ['cancelled', 'timed_out']:
		return 'errored'
	if conclusion == 'action_required':
		return 'warned'
	if conclusion == 'failure':
		return 'failed'
	return 'passed'
