METADATA =\
{
	'name': 'chroma-feedback',
	'description': 'Turn your RGB powered hardware into an extreme feedback device for continuous integration',
	'version': '6.0.1',
	'license': 'GPL-3.0',
	'keywords': 'appveyor circle codeship github gitlab jenkins teamcity travis ci notification indication',
	'author': 'Henry Ruhs',
	'author_email': 'info@redaxmedia.com',
	'url': 'https://github.com/redaxmedia/chroma-feedback'
}


def get(key : str) -> str:
	return METADATA[key]
