from chroma_feedback import producer

METADATA =\
{
	'name': 'chroma-feedback',
	'description': 'Turn your RGB powered hardware into a status indicator for continuous integration, continuous deployment and infrastructure monitoring',
	'version': '13.0.4',
	'license': 'MIT',
	'keywords': ' '.join(producer.ALL),
	'author': 'Henry Ruhs',
	'author_email': 'info@henryruhs.com',
	'url': 'https://chroma-feedback.com'
}


def get(key : str) -> str:
	return METADATA[key]
