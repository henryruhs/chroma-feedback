from chroma_feedback import helper
from chroma_feedback.typing import Producer, Status


def normalize_data(slug : str, status : str) -> Producer:
	return\
	{
		'name': 'datadog',
		'slug': slug,
		'url': None,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> Status:
	status = helper.to_lower_case(status).replace(' ', '_')

	if status == 'skipped':
		return 'skipped'
	if status == 'no_data':
		return 'errored'
	if status == 'warn':
		return 'warned'
	if status == 'alert':
		return 'failed'
	return 'passed'
