import pytest
import os
import argparse
from typing import get_args

from chroma_feedback.producer.circle import circle
from chroma_feedback.typing import Status


def test_run_one() -> None:
	if os.environ.get('CIRCLE_TOKEN'):
		circle.core.ARGS = argparse.Namespace(
			circle_host = 'https://circleci.com',
			circle_organization = None,
			circle_slug =
			[
				'github/henryruhs/chroma-feedback'
			],
			circle_token = os.environ.get('CIRCLE_TOKEN')
		)
		result = circle.core.run()

		assert result[0]['name'] == 'circle'
		assert result[0]['slug'] == 'gh/henryruhs/chroma-feedback/lint-and-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('CIRCLE_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('CIRCLE_TOKEN'):
		circle.core.ARGS = argparse.Namespace(
			circle_host = 'https://circleci.com',
			circle_organization = 'github/henryruhs',
			circle_slug = None,
			circle_token = os.environ.get('CIRCLE_TOKEN')
		)
		result = circle.core.run()

		assert result[0]['name'] == 'circle'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('CIRCLE_TOKEN is not defined')
