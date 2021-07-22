from chroma_feedback import producer

METADATA =\
{
	'name': 'chroma-feedback',
	'description': 'Turn your RGB powered hardware into an build indicator for continuous integration',
	'version': '10.2.0',
	'license': 'MIT',
	'keywords': ' '.join(producer.__all__),
	'author': 'Henry Ruhs',
	'author_email': 'info@redaxmedia.com',
	'url': 'https://github.com/redaxmedia/chroma-feedback'
}


def get(key : str) -> str:
	return METADATA[key]
