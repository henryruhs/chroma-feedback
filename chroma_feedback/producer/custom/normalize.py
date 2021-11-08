from chroma_feedback.typing import Status, Producer


def normalize_data(slug : str, active : bool, status : Status) -> Producer:
	return\
	{
		'producer': 'custom',
		'slug': slug,
		'active': active,
		'status': status
	}
