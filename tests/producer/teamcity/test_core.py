import pytest
import os
import argparse
from typing import get_args

from chroma_feedback.producer import teamcity
from chroma_feedback.typing import Status


def test_run_one() -> None:
	if os.environ.get('TEAMCITY_TOKEN'):
		teamcity.core.ARGS = argparse.Namespace(
			teamcity_host = 'https://teamcity.jetbrains.com',
			teamcity_slug =
			[
				'IntellijIdeaPlugins_MicroPythonPlugin'
			],
			teamcity_token = os.environ.get('TEAMCITY_TOKEN')
		)
		result = teamcity.core.run()

		assert result[0]['name'] == 'teamcity'
		assert result[0]['slug']
		assert 'IntellijIdeaPlugins_MicroPythonPlugin' in result[0]['url']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('TEAMCITY_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('TEAMCITY_TOKEN'):
		teamcity.core.ARGS = argparse.Namespace(
			teamcity_host = 'https://teamcity.jetbrains.com',
			teamcity_slug = None,
			teamcity_token = os.environ.get('TEAMCITY_TOKEN')
		)
		result = teamcity.core.run()

		assert result[0]['name'] == 'teamcity'
		assert result[0]['slug']
		assert result[0]['url']
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'teamcity'
		assert result[1]['slug']
		assert result[0]['url']
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('TEAMCITY_TOKEN is not defined')
