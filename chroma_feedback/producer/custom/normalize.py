from typing import Any, Dict


def normalize_data(slug : str, active : bool, status : str) -> Dict[str, Any]:
	return\
	{
		'producer': 'custom',
		'slug': slug,
		'active': active,
		'status': status
	}
