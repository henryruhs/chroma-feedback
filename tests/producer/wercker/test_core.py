import pytest
import os
import argparse
from typing import get_args

from chroma_feedback.producer import wercker
from chroma_feedback.typing import Status


def test_run_one() -> None:
	if os.environ.get('WERCKER_TOKEN'):
		wercker.core.ARGS = argparse.Namespace(
			wercker_host = 'https://app.wercker.com',
			wercker_slug =
			[
				'redaxmedia/chroma-feedback'
			],
			wercker_token = os.environ.get('WERCKER_TOKEN')
		)
		result = wercker.core.run()

		assert result[0]['name'] == 'wercker'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('WERCKER_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('WERCKER_TOKEN'):
		wercker.core.ARGS = argparse.Namespace(
			wercker_host = 'https://app.wercker.com',
			wercker_slug =
			[
				'redaxmedia'
			],
			wercker_token = os.environ.get('WERCKER_TOKEN')
		)
		result = wercker.core.run()

		assert result[0]['name'] == 'wercker'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('WERCKER_TOKEN is not defined')
