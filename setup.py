#!/usr/bin/env python3

from setuptools import setup

setup(
	name = 'chroma-feedback',
	description = 'Turn your Razer keyboard, mouse or headphone into a extreme feedback device for Travis CI',
	version = '1.0.0',
	license = 'GPL-3.0',
	url='https://github.com/redaxmedia/chroma-feedback',
	download_url='https://github.com/redaxmedia/chroma-feedback/archive/master.zip',
	author = 'Henry Ruhs',
	author_email = 'info@redaxmedia.com',
	keywords =
	[
		'razer',
		'chroma',
		'travis-ci'
	],
	packages =
	[
		'src'
	],
	scripts =
	[
		'bin/chroma-feedback'
	]
)
