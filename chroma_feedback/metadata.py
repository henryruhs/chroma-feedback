metadata =\
{
	'name': 'chroma-feedback',
	'description': 'Turn your RGB powered hardware into an extreme feedback device for continuous integration',
	'version': '4.2.0',
	'license': 'GPL-3.0',
	'keywords': 'appveyor circle github gitlab jenkins teamcity travis ci notification indication',
	'author': 'Henry Ruhs',
	'author_email': 'info@redaxmedia.com',
	'url': 'https://github.com/redaxmedia/chroma-feedback'
}


def get(key):
	return metadata[key]
