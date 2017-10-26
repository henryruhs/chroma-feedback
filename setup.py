#!/usr/bin/env python3

from setuptools import setup
from pypandoc import convert

setup(
	name = 'chroma-feedback',
	description = 'Turn your Razer keyboard, mouse or headphone into a extreme feedback device for Travis CI',
	long_description = convert('README.md', 'rst'),
	version = '1.0.2',
	license = 'GPL-3.0',
	url = 'https://github.com/redaxmedia/chroma-feedback',
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
	install_requires =
	[
		'pypandoc'
	],
	scripts =
	[
		'bin/chroma-feedback'
	]
)
