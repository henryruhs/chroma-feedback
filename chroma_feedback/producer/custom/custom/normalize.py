from chroma_feedback.types import Producer, Status


def normalize_data(slug : str, url : str, status : Status) -> Producer:
	return\
	{
		'name': 'custom',
		'slug': slug,
		'url': url,
		'status': status
	}
