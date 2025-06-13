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
		'chroma_feedback.producer.appveyor.appveyor',
		'chroma_feedback.producer.atlassian.bamboo',
		'chroma_feedback.producer.atlassian.bitbucket',
		'chroma_feedback.producer.betterstack.betterstack',
		'chroma_feedback.producer.buddy.buddy',
		'chroma_feedback.producer.circle.circle',
		'chroma_feedback.producer.cloudbees.codeship',
		'chroma_feedback.producer.custom.custom',
		'chroma_feedback.producer.datadog.datadog',
		'chroma_feedback.producer.gitlab.gitlab',
		'chroma_feedback.producer.heroku.heroku',
		'chroma_feedback.producer.jenkins.jenkins',
		'chroma_feedback.producer.jetbrains.teamcity',
		'chroma_feedback.producer.microsoft.azure',
		'chroma_feedback.producer.microsoft.github',
		'chroma_feedback.producer.netlify.netlify',
		'chroma_feedback.producer.travis.travis',
		'chroma_feedback.producer.uptimerobot.uptimerobot',
		'chroma_feedback.producer.vercel.vercel',
		'chroma_feedback.consumer',
		'chroma_feedback.consumer.agile_innovative.blinkstick',
		'chroma_feedback.consumer.compulab.fit_statusb',
		'chroma_feedback.consumer.elgato.streamdeck',
		'chroma_feedback.consumer.embrava.blynclight',
		'chroma_feedback.consumer.embrava.blynclight_mini',
		'chroma_feedback.consumer.embrava.blynclight_plus',
		'chroma_feedback.consumer.gigabyte.rgb_fusion2',
		'chroma_feedback.consumer.kuando.busylight_alpha',
		'chroma_feedback.consumer.kuando.busylight_omega',
		'chroma_feedback.consumer.lifx.lifx',
		'chroma_feedback.consumer.luxafor.flag',
		'chroma_feedback.consumer.luxafor.mute',
		'chroma_feedback.consumer.luxafor.orb',
		'chroma_feedback.consumer.magic.hue',
		'chroma_feedback.consumer.muteme.muteme',
		'chroma_feedback.consumer.muteme.muteme_mini',
		'chroma_feedback.consumer.mutesync.mutesync',
		'chroma_feedback.consumer.nanoleaf.nanoleaf',
		'chroma_feedback.consumer.philips.hue',
		'chroma_feedback.consumer.plantronics.status_indicator',
		'chroma_feedback.consumer.razer.chroma',
		'chroma_feedback.consumer.signify.wiz',
		'chroma_feedback.consumer.thingm.blink1',
		'chroma_feedback.consumer.xiaomi.yeelight'
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
		'busylight-for-humans==0.35.4',
		'lifxlan==1.2.8',
		'liquidctl==1.15.0',
		'nanoleafapi==2.1.2',
		'phue==1.1',
		'python-magichue==0.3.2',
		'pyqt6==6.9.1',
		'pywizlight==0.6.2',
		'requests==2.32.3 ',
		'streamdeck==0.9.6',
		'yeelight==0.7.16'
	],
	tests_require =
	[
		'flake8==7.2.0',
		'mock==5.2.0',
		'mypy==1.16.0',
		'pytest==8.4.0',
		'pytest-cov==6.1.1',
		'pytest-dotenv==0.5.2',
		'pytest-mock==3.14.1',
		'types-mock==5.2.0.20250516',
		'types-requests==2.32.0.20250602'
	]
)
