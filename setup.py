#!/usr/bin/env python3

from setuptools import setup
from src import metadata

try:
	from pypandoc import convert
	long_description = convert('README.md', 'rst')
except ImportError:
	long_description = open('README.md').read()

setup(
	name = metadata.get('name'),
	description =  metadata.get('description'),
	long_description = long_description,
	version = metadata.get('version'),
	license = metadata.get('license'),
	keywords = metadata.get('keywords'),
	author = metadata.get('author'),
	author_email = metadata.get('author_email'),
	url = metadata.get('url'),
	packages =
	[
		'src',
		'src/provider'
	],
	scripts =
	[
		'bin/chroma-feedback'
	],
	install_requires =
	[
		'requests'
	],
	tests_require =
	[
		'pylint',
		'pytest',
		'mock'
	]
)
