from typing import Any, Dict
from chroma_feedback import helper
from chroma_feedback.typing import StatusType


def normalize_data(slug : str, status : str) -> Dict[str, Any]:
	return\
	{
		'producer': 'buddy',
		'slug': slug,
		'active': True,
		'status': normalize_status(status)
	}


def normalize_status(status : str) -> StatusType:
	status = helper.to_lower_case(status)

	if status == 'inprogress':
		return 'started'
	if status == 'failed':
		return 'failed'
	return 'passed'
