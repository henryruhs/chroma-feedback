from chroma_feedback.producer import __all__ as producer

METADATA =\
{
	'name': 'chroma-feedback',
	'description': 'Turn your RGB powered hardware into an build indicator for continuous integration',
	'version': '10.0.0',
	'license': 'MIT',
	'keywords': ' '.join(producer),
	'author': 'Henry Ruhs',
	'author_email': 'info@redaxmedia.com',
	'url': 'https://github.com/redaxmedia/chroma-feedback'
}


def get(key : str) -> str:
	return METADATA[key]
