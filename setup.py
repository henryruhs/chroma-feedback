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
		'chroma_feedback.producer.bitbucket',
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
		'chroma_feedback.consumer.luxafor_flag',
		'chroma_feedback.consumer.magic_hue',
		'chroma_feedback.consumer.nanoleaf_light',
		'chroma_feedback.consumer.philips_hue',
		'chroma_feedback.consumer.razer_chroma',
		'chroma_feedback.consumer.thingm_blink',
		'chroma_feedback.consumer.wiz_light',
		'chroma_feedback.consumer.xiaomi_yeelight'
	],
	scripts =
	[
		'bin/chroma-feedback'
	],
	install_requires =
	[
		'asyncio==3.4.3',
		'busylight-for-humans==0.8.2',
		'blink1==0.3.1',
		'blinkstick==1.2.0',
		'lifxlan==1.2.5',
		'nanoleafapi==2.0.0',
		'phue==1.1',
		'pillow==8.1.2',
		'python-magichue==0.2.9.3',
		'pywizlight==0.4.5',
		'requests==2.25.1',
		'yeelight==0.5.4'
	],
	tests_require =
	[
		'coveralls==3.0.1',
		'pylint==2.7.2',
		'pytest==6.2.2',
		'pytest-cov==2.11.1',
		'pytest-mock==3.5.1',
		'mock==4.0.3',
		'mypy==0.812'
	]
)
