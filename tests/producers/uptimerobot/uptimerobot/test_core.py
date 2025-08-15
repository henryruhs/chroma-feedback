import os
from typing import get_args

import pytest

from chroma_feedback.producers.uptimerobot import uptimerobot
from chroma_feedback.types import Status


def test_run_one() -> None:
	if os.environ.get('UPTIMEROBOT_TOKEN'):
		uptimerobot.core.ARGS =\
		{
			'uptimerobot_host': 'https://api.uptimerobot.com',
			'uptimerobot_slug':
			[
				'chroma-feedback-test'
			],
			'uptimerobot_token': os.environ.get('UPTIMEROBOT_TOKEN')
		}
		result = uptimerobot.core.run()

		assert result[0]['name'] == 'uptimerobot'
		assert result[0]['slug'] == 'chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('UPTIMEROBOT_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('UPTIMEROBOT_TOKEN'):
		uptimerobot.core.ARGS =\
		{
			'uptimerobot_host': 'https://api.uptimerobot.com',
			'uptimerobot_slug': None,
			'uptimerobot_token': os.environ.get('UPTIMEROBOT_TOKEN')
		}
		result = uptimerobot.core.run()

		assert result[0]['name'] == 'uptimerobot'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('UPTIMEROBOT_TOKEN is not defined')
