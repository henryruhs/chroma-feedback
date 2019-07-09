metadata =\
{
	'name': 'chroma-feedback',
	'description': 'Turn your Philips Hue lights, Razer Chroma devices or ThingM Blink lights into extreme feedback devices',
	'version': '4.0.0',
	'license': 'GPL-3.0',
	'keywords': 'appveyor circle github gitlab jenkins teamcity travis ci notification indication',
	'author': 'Henry Ruhs',
	'author_email': 'info@redaxmedia.com',
	'url': 'https://github.com/redaxmedia/chroma-feedback'
}


def get(key):
	return metadata[key]
