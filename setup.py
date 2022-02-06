#!/usr/bin/env python3

from setuptools import setup
from chroma_feedback import metadata
from chroma_feedback.install import InstallCommand

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
		'chroma_feedback.producer.azure',
		'chroma_feedback.producer.bamboo',
		'chroma_feedback.producer.bitbucket',
		'chroma_feedback.producer.buddy',
		'chroma_feedback.producer.circle',
		'chroma_feedback.producer.codeship',
		'chroma_feedback.producer.datadog',
		'chroma_feedback.producer.github',
		'chroma_feedback.producer.gitlab',
		'chroma_feedback.producer.jenkins',
		'chroma_feedback.producer.teamcity',
		'chroma_feedback.producer.travis',
		'chroma_feedback.producer.wercker',
		'chroma_feedback.consumer',
		'chroma_feedback.consumer.agile_innovative_blinkstick',
		'chroma_feedback.consumer.elgato_streamdeck',
		'chroma_feedback.consumer.embrava_blynclight',
		'chroma_feedback.consumer.kuando_busylight',
		'chroma_feedback.consumer.lifx_light',
		'chroma_feedback.consumer.luxafor_flag',
		'chroma_feedback.consumer.magic_hue',
		'chroma_feedback.consumer.nanoleaf_light',
		'chroma_feedback.consumer.philips_hue',
		'chroma_feedback.consumer.razer_chroma',
		'chroma_feedback.consumer.thingm_blink1',
		'chroma_feedback.consumer.wiz_light',
		'chroma_feedback.consumer.xiaomi_yeelight'
	],
	cmdclass =
	{
		'install': InstallCommand
	},
	entry_points =
	{
		'console_scripts':
		[
			'chroma-feedback = chroma_feedback.core:cli',
		]
	},
	install_requires =
	[
		'busylight-for-humans==0.15.0',
		'lifxlan==1.2.7',
		'nanoleafapi==2.1.1',
		'phue==1.1',
		'python-magichue==0.2.9.3',
		'pyqt5==5.15.6',
		'pywizlight==0.5.0',
		'requests==2.27.1',
		'streamdeck==0.9.0 ',
		'yeelight==0.7.8'
	],
	tests_require =
	[
		'flake8==4.0.1 ',
		'mock==4.0.3 ',
		'mypy==0.931 ',
		'pyqt5-stubs==5.15.2.0',
		'pytest==6.2.5 ',
		'pytest-cov==3.0.0 ',
		'pytest-mock==3.7.0 ',
		'types-mock==4.0.9 ',
		'types-requests==2.27.7'
	]
)
