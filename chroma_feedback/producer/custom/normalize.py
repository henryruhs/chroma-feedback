from chroma_feedback.typing import Status, Producer


def normalize_data(slug : str, url : str, status : Status) -> Producer:
	return\
	{
		'producer': 'custom',
		'slug': slug,
		'url': url,
		'status': status
	}
