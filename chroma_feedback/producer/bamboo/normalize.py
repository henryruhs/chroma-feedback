from chroma_feedback import helper
from chroma_feedback.typing import StatusType, ProducerModel


def normalize_data(slug : str, status : str) -> ProducerModel:
	return\
	{
		'producer': 'bamboo',
		'slug': slug,
		'active': True,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> StatusType:
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
