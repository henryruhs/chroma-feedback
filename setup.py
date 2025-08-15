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
		'chroma_feedback.producers',
		'chroma_feedback.producers.appveyor.appveyor',
		'chroma_feedback.producers.atlassian.bamboo',
		'chroma_feedback.producers.atlassian.bitbucket',
		'chroma_feedback.producers.betterstack.betterstack',
		'chroma_feedback.producers.buddy.buddy',
		'chroma_feedback.producers.circle.circle',
		'chroma_feedback.producers.cloudbees.codeship',
		'chroma_feedback.producers.custom.custom',
		'chroma_feedback.producers.datadog.datadog',
		'chroma_feedback.producers.gitlab.gitlab',
		'chroma_feedback.producers.heroku.heroku',
		'chroma_feedback.producers.jenkins.jenkins',
		'chroma_feedback.producers.jetbrains.teamcity',
		'chroma_feedback.producers.microsoft.azure',
		'chroma_feedback.producers.microsoft.github',
		'chroma_feedback.producers.netlify.netlify',
		'chroma_feedback.producers.travis.travis',
		'chroma_feedback.producers.uptimerobot.uptimerobot',
		'chroma_feedback.producers.vercel.vercel',
		'chroma_feedback.consumers',
		'chroma_feedback.consumers.agile_innovative.blinkstick',
		'chroma_feedback.consumers.compulab.fit_statusb',
		'chroma_feedback.consumers.elgato.streamdeck',
		'chroma_feedback.consumers.embrava.blynclight',
		'chroma_feedback.consumers.embrava.blynclight_mini',
		'chroma_feedback.consumers.embrava.blynclight_plus',
		'chroma_feedback.consumers.gigabyte.rgb_fusion2',
		'chroma_feedback.consumers.kuando.busylight_alpha',
		'chroma_feedback.consumers.kuando.busylight_omega',
		'chroma_feedback.consumers.lifx.lifx',
		'chroma_feedback.consumers.luxafor.flag',
		'chroma_feedback.consumers.luxafor.mute',
		'chroma_feedback.consumers.luxafor.orb',
		'chroma_feedback.consumers.magic.hue',
		'chroma_feedback.consumers.muteme.muteme',
		'chroma_feedback.consumers.muteme.muteme_mini',
		'chroma_feedback.consumers.mutesync.mutesync',
		'chroma_feedback.consumers.nanoleaf.nanoleaf',
		'chroma_feedback.consumers.philips.hue',
		'chroma_feedback.consumers.plantronics.status_indicator',
		'chroma_feedback.consumers.razer.chroma',
		'chroma_feedback.consumers.signify.wiz',
		'chroma_feedback.consumers.thingm.blink1',
		'chroma_feedback.consumers.xiaomi.yeelight'
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
