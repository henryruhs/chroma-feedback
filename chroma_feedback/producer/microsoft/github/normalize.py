from chroma_feedback import helper
from chroma_feedback.typing import Producer, Status


def normalize_data(slug : str, url : str, status : str, conclusion : str) -> Producer:
	return\
	{
		'name': 'microsoft.github',
		'slug': slug,
		'url': url,
		'status': normalize_status(status, conclusion)
	}


def normalize_status(status : str, conclusion : str) -> Status:
	status = helper.to_lower_case(status)
	conclusion = helper.to_lower_case(conclusion)

	if conclusion == 'skipped':
		return 'skipped'
	if status in ['in_progress', 'queued']:
		return 'started'
	if conclusion in ['cancelled', 'stale']:
		return 'errored'
	if conclusion in ['action_required', 'timed_out']:
		return 'warned'
	if conclusion == 'failure':
		return 'failed'
	return 'passed'
