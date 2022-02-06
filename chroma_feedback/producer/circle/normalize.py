from chroma_feedback import helper
from chroma_feedback.typing import Producer, Status


def normalize_data(slug : str, status : str) -> Producer:
	return\
	{
		'name': 'circle',
		'slug': slug,
		'url': None,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> Status:
	status = helper.to_lower_case(status)

	if status == 'no_tests':
		return 'skipped'
	if status in ['queued', 'retried', 'running', 'scheduled']:
		return 'started'
	if status == 'canceled':
		return 'errored'
	if status == 'timedout':
		return 'warned'
	if status in ['failed', 'infrastructure_fail']:
		return 'failed'
	return 'passed'

