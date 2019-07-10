#!/usr/bin/env python3

from setuptools import setup
from chroma_feedback import metadata

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
		'chroma_feedback',
		'chroma_feedback.provider',
		'chroma_feedback.consumer'
	],
	scripts =
	[
		'bin/chroma-feedback'
	],
	install_requires =
	[
		'requests'
	],
	tests_require=
	[
		'pylint',
		'pytest',
		'pytest-cov',
		'pytest-mock',
		'mock'
	]
)
