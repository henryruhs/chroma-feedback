#!/usr/bin/env python3

from setuptools import setup
from chroma_feedback import metadata

try:
	from pypandoc import convert_file
	long_description = convert_file('README.md', 'rst')
except ImportError:
	long_description = open('README.md').read()

setup(
	name = metadata.get('name'),
	description = metadata.get('description'),
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
		'chroma_feedback.provider.appveyor',
		'chroma_feedback.provider.circle',
		'chroma_feedback.provider.codeship',
		'chroma_feedback.provider.github',
		'chroma_feedback.provider.gitlab',
		'chroma_feedback.provider.jenkins',
		'chroma_feedback.provider.teamcity',
		'chroma_feedback.provider.travis',
		'chroma_feedback.consumer',
		'chroma_feedback.consumer.agile_innovative_blinkstick',
		'chroma_feedback.consumer.lifx_light',
		'chroma_feedback.consumer.philips_hue',
		'chroma_feedback.consumer.razer_chroma',
		'chroma_feedback.consumer.thingm_blink',
		'chroma_feedback.consumer.xiaomi_yeelight'
	],
	scripts =
	[
		'bin/chroma-feedback'
	],
	install_requires =
	[
		'blink1',
		'blinkstick',
		'lifxlan',
		'phue',
		'requests',
		'yeelight'
	],
	tests_require =
	[
		'coveralls',
		'pylint',
		'pytest',
		'pytest-cov',
		'pytest-mock',
		'mock',
		'mypy'
	]
)
