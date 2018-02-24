#!/usr/bin/env python3

from setuptools import setup
from src.metadata import metadata

try:
	from pypandoc import convert
	long_description = convert('README.md', 'rst')
except ImportError:
	long_description = open('README.md').read()

setup(
	name = metadata['name'],
	description =  metadata['description'],
	long_description = long_description,
	version = metadata['version'],
	license = metadata['license'],
	keywords = metadata['keywords'],
	author = metadata['author'],
	author_email = metadata['author_email'],
	url = metadata['url'],
	packages =
	[
		'src'
	],
	scripts =
	[
		'bin/chroma-feedback'
	],
	install_requires =
	[
		'requests'
	]
)
