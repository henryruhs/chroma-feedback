from chroma_feedback import helper
from chroma_feedback.typing import Producer, Status


def normalize_data(slug : str, url : str, status : str, is_paused : bool, is_running : bool) -> Producer:
	return\
	{
		'name': 'jetbrains.teamcity',
		'slug': slug,
		'url': url,
		'status': normalize_status(status, is_paused, is_running)
	}


def normalize_status(status : str, is_paused : bool, is_running : bool) -> Status:
	status = helper.to_lower_case(status)

	if is_paused:
		return 'skipped'
	if is_running:
		return 'started'
	if status == 'error':
		return 'errored'
	if status == 'failure':
		return 'failed'
	return 'passed'
