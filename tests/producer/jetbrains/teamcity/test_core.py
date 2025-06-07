import argparse
import os
from typing import get_args

import pytest

from chroma_feedback.producer.jetbrains import teamcity
from chroma_feedback.types import Status


def test_run_one() -> None:
	if os.environ.get('JETBRAINS_TEAMCITY_TOKEN'):
		teamcity.core.ARGS =\
		{
			'jetbrains_teamcity_host': 'https://teamcity.jetbrains.com',
			'jetbrains_teamcity_slug':
			[
				'IntellijIdeaPlugins_MicroPythonPlugin'
			],
			'jetbrains_teamcity_token': os.environ.get('JETBRAINS_TEAMCITY_TOKEN')
		}
		result = teamcity.core.run()

		assert result[0]['name'] == 'jetbrains.teamcity'
		assert result[0]['slug']
		assert 'IntellijIdeaPlugins_MicroPythonPlugin' in result[0]['url']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('JETBRAINS_TEAMCITY_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('JETBRAINS_TEAMCITY_TOKEN'):
		teamcity.core.ARGS =\
		{
			'jetbrains_teamcity_host': 'https://teamcity.jetbrains.com',
			'jetbrains_teamcity_slug': None,
			'jetbrains_teamcity_token': os.environ.get('JETBRAINS_TEAMCITY_TOKEN')
		}
		result = teamcity.core.run()

		assert result[0]['name'] == 'jetbrains.teamcity'
		assert result[0]['slug']
		assert result[0]['url']
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'jetbrains.teamcity'
		assert result[1]['slug']
		assert result[0]['url']
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('JETBRAINS_TEAMCITY_TOKEN is not defined')
