from chroma_feedback.typing import ProducerModel


def normalize_data(slug : str, active : bool, status : str) -> ProducerModel:
	return\
	{
		'producer': 'custom',
		'slug': slug,
		'active': active,
		'status': status
	}
