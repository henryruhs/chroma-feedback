METADATA =\
{
	'name': 'chroma-feedback',
	'description': 'Turn your RGB powered hardware into an build indicator for continuous integration',
	'version': '7.4.0',
	'license': 'GPL-3.0',
	'keywords': 'appveyor bamboo circle codeship github gitlab jenkins teamcity travis',
	'author': 'Henry Ruhs',
	'author_email': 'info@redaxmedia.com',
	'url': 'https://github.com/redaxmedia/chroma-feedback'
}


def get(key : str) -> str:
	return METADATA[key]
