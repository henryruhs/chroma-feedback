from chroma_feedback.typing import StatusType, ProducerModel


def normalize_data(slug : str, active : bool, status : StatusType) -> ProducerModel:
	return\
	{
		'producer': 'custom',
		'slug': slug,
		'active': active,
		'status': status
	}
