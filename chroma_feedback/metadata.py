from chroma_feedback import producer

METADATA =\
{
	'name': 'chroma-feedback',
	'description': 'Turn your RGB powered hardware into a status indicator for continuous integration, continuous deployment and infrastructure monitoring',
	'version': '11.0.1',
	'license': 'MIT',
	'keywords': ' '.join(producer.__all__),
	'author': 'Henry Ruhs',
	'author_email': 'info@redaxmedia.com',
	'url': 'https://chroma-feedback.com'
}


def get(key : str) -> str:
	return METADATA[key]
