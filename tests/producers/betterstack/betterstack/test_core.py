import os
from typing import get_args

import pytest

from chroma_feedback.producers.betterstack import betterstack
from chroma_feedback.types import Status


def test_run_one() -> None:
	if os.environ.get('BETTERSTACK_TOKEN'):
		betterstack.core.ARGS =\
		{
			'betterstack_host': 'https://uptime.betterstack.com',
			'betterstack_slug':
			[
				'chroma-feedback-test'
			],
			'betterstack_token': os.environ.get('BETTERSTACK_TOKEN')
		}
		result = betterstack.core.run()

		assert result[0]['name'] == 'betterstack'
		assert result[0]['slug'] == 'chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('BETTERSTACK_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('BETTERSTACK_TOKEN'):
		betterstack.core.ARGS =\
		{
			'betterstack_host': 'https://uptime.betterstack.com',
			'betterstack_slug': None,
			'betterstack_token': os.environ.get('BETTERSTACK_TOKEN')
		}
		result = betterstack.core.run()

		assert result[0]['name'] == 'betterstack'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('BETTERSTACK_TOKEN is not defined')
