import pytest
import os
import argparse
from typing import get_args

from chroma_feedback.producer import travis
from chroma_feedback.typing import Status

def test_run_one() -> None:
	if os.environ.get('TRAVIS_TOKEN'):
		travis.core.ARGS = argparse.Namespace(
			travis_host = 'https://api.travis-ci.com',
			travis_slug =
			[
				'redaxmedia/chroma-feedback'
			],
			travis_token = os.environ.get('TRAVIS_TOKEN')
		)
		result = travis.core.run()

		assert result[0]['name'] == 'travis'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('TRAVIS_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('TRAVIS_TOKEN'):
		travis.core.ARGS = argparse.Namespace(
			travis_host ='https://api.travis-ci.com',
			travis_slug =
			[
				'redaxmedia'
			],
			travis_token = os.environ.get('TRAVIS_TOKEN')
		)
		result = travis.core.run()

		assert result[0]['name'] == 'travis'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('TRAVIS_TOKEN is not defined')
