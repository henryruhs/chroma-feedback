from typing import Optional

from chroma_feedback import producers

METADATA =\
{
	'name': 'chroma-feedback',
	'description': 'Turn your RGB powered hardware into a status indicator for continuous integration, continuous deployment and infrastructure monitoring',
	'version': '13.6.0',
	'license': 'MIT',
	'keywords': ' '.join(producers.ALL),
	'author': 'Henry Ruhs',
	'author_email': 'info@henryruhs.com',
	'url': 'https://github.com/henryruhs/chroma-feedback'
}


def get(key : str) -> Optional[str]:
	if key in METADATA:
		return METADATA.get(key)
	return None
