#!/usr/bin/env python3

from setuptools import setup
from src.version import __version__

try:
	from pypandoc import convert
	long_description = convert('README.md', 'rst')
except ImportError:
	long_description = open('README.md').read()

setup(
	name = 'chroma-feedback',
	description = 'Turn your Razer keyboard, mouse or headphone into a extreme feedback device for Travis CI',
	long_description = long_description,
	version = __version__,
	license = 'GPL-3.0',
	url = 'https://github.com/redaxmedia/chroma-feedback',
	author = 'Henry Ruhs',
	author_email = 'info@redaxmedia.com',
	keywords = 'razer chroma travis ci',
	packages =
	[
		'src'
	],
	scripts =
	[
		'bin/chroma-feedback'
	]
)
