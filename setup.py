#!/usr/bin/env python3

from setuptools import setup
from chroma_feedback import metadata

setup(
	name = metadata.get('name'),
	description = metadata.get('description'),
	long_description = open('README.md').read(),
	long_description_content_type = 'text/markdown',
	version = metadata.get('version'),
	license = metadata.get('license'),
	keywords = metadata.get('keywords'),
	author = metadata.get('author'),
	author_email = metadata.get('author_email'),
	url = metadata.get('url'),
	packages =
	[
		'chroma_feedback',
		'chroma_feedback.producer',
		'chroma_feedback.producer.appveyor',
		'chroma_feedback.producer.bamboo',
		'chroma_feedback.producer.circle',
		'chroma_feedback.producer.codeship',
		'chroma_feedback.producer.github',
		'chroma_feedback.producer.gitlab',
		'chroma_feedback.producer.jenkins',
		'chroma_feedback.producer.teamcity',
		'chroma_feedback.producer.travis',
		'chroma_feedback.producer.wercker',
		'chroma_feedback.consumer',
		'chroma_feedback.consumer.agile_innovative_blinkstick',
		'chroma_feedback.consumer.lifx_light',
		'chroma_feedback.consumer.magic_hue',
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
		'python-magichue',
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
