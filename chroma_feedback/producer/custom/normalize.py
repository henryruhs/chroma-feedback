from typing import Any, Dict


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'custom',
		'slug': project['slug'],
		'active': project['active'],
		'status': project['status']
	}
