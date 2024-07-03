import argparse
import os
from typing import get_args

import pytest

from chroma_feedback.producer.appveyor import appveyor
from chroma_feedback.typing import Status


def test_run_one() -> None:
	if os.environ.get('APPVEYOR_TOKEN'):
		appveyor.core.ARGS = argparse.Namespace(
			appveyor_host = 'https://ci.appveyor.com',
			appveyor_slug =
			[
				'henryruhs/chroma-feedback'
			],
			appveyor_token = os.environ.get('APPVEYOR_TOKEN')
		)
		result = appveyor.core.run()

		assert result[0]['name'] == 'appveyor'
		assert result[0]['slug'] == 'henryruhs/chroma-feedback'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('APPVEYOR_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('APPVEYOR_TOKEN'):
		appveyor.core.ARGS = argparse.Namespace(
			appveyor_host = 'https://ci.appveyor.com',
			appveyor_slug = None,
			appveyor_token = os.environ.get('APPVEYOR_TOKEN')
		)
		result = appveyor.core.run()

		assert result[0]['name'] == 'appveyor'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('APPVEYOR_TOKEN is not defined')
