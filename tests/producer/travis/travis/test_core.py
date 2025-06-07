import argparse
import os
from typing import get_args

import pytest

from chroma_feedback.producer.travis import travis
from chroma_feedback.types import Status


def test_run_one() -> None:
	if os.environ.get('TRAVIS_TOKEN'):
		travis.core.ARGS =\
		{
			'travis_host': 'https://api.travis-ci.com',
			'travis_slug':
			[
				'henryruhs/chroma-feedback'
			],
			'travis_token': os.environ.get('TRAVIS_TOKEN')
		}
		result = travis.core.run()

		assert result[0]['name'] == 'travis'
		assert result[0]['slug'] == 'henryruhs/chroma-feedback'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('TRAVIS_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('TRAVIS_TOKEN'):
		travis.core.ARGS =\
		{
			'travis_host': 'https://api.travis-ci.com',
			'travis_slug':
			[
				'henryruhs'
			],
			'travis_token': os.environ.get('TRAVIS_TOKEN')
		}
		result = travis.core.run()

		assert result[0]['name'] == 'travis'
		assert result[0]['slug'] == 'henryruhs/chroma-feedback'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('TRAVIS_TOKEN is not defined')
