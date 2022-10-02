from chroma_feedback import helper
from chroma_feedback.typing import Producer, Status


def normalize_data(slug : str, status : str) -> Producer:
	return\
	{
		'name': 'cloudbees.codeship',
		'slug': slug,
		'url': None,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> Status:
	status = helper.to_lower_case(status)

	if status == 'ignored':
		return 'skipped'
	if status in ['initiated', 'testing', 'waiting']:
		return 'started'
	if status in ['error', 'blocked']:
		return 'errored'
	if status in ['failed', 'infrastructure_failure']:
		return 'failed'
	return 'passed'
