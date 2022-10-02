from chroma_feedback import helper
from chroma_feedback.typing import Producer, Status


def normalize_data(slug : str, status : str) -> Producer:
	return\
	{
		'name': 'atlassian.bamboo',
		'slug': slug,
		'url': None,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> Status:
	status = helper.to_lower_case(status)

	if status == 'unknown':
		return 'errored'
	if status == 'failed':
		return 'failed'
	return 'passed'


def normalize_slug(slug : str) -> str:
	if '-' in slug:
		return slug + '-latest'
	return slug
