import pytest
import os
from typing import get_args

from chroma_feedback.producer.travis.core import fetch
from chroma_feedback.typing import Status


def test_fetch_slug() -> None:
	if os.environ.get('TRAVIS_TOKEN'):
		result = fetch('https://api.travis-ci.com', 'redaxmedia/chroma-feedback', os.environ.get('TRAVIS_TOKEN'))

		assert result[0]['name'] == 'travis'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('TRAVIS_TOKEN is not defined')


def test_fetch_user() -> None:
	if os.environ.get('TRAVIS_TOKEN'):
		result = fetch('https://api.travis-ci.com', 'redaxmedia', os.environ.get('TRAVIS_TOKEN'))

		assert result[0]['name'] == 'travis'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('TRAVIS_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
