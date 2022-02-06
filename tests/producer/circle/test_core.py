import os
import pytest
from typing import get_args

from chroma_feedback.producer.circle.core import fetch
from chroma_feedback.typing import Status


def test_fetch_slug() -> None:
	if os.environ.get('CIRCLE_TOKEN'):
		result = fetch('https://circleci.com', None, 'github/redaxmedia/chroma-feedback', None, os.environ.get('CIRCLE_TOKEN'))

		assert result[0]['name'] == 'circle'
		assert result[0]['slug'] == 'gh/redaxmedia/chroma-feedback/lint-and-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('CIRCLE_TOKEN is not defined')


def test_fetch_slug_mine() -> None:
	if os.environ.get('CIRCLE_TOKEN'):
		result = fetch('https://circleci.com', None, 'github/redaxmedia/chroma-feedback', 'mine', os.environ.get('CIRCLE_TOKEN'))

		assert result[0]['name'] == 'circle'
		assert result[0]['slug'] == 'gh/redaxmedia/chroma-feedback/lint-and-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('CIRCLE_TOKEN is not defined')


def test_fetch_organization() -> None:
	if os.environ.get('CIRCLE_TOKEN'):
		result = fetch('https://circleci.com', 'github/redaxmedia', None, None, os.environ.get('CIRCLE_TOKEN'))

		assert result[0]['name'] == 'circle'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('CIRCLE_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None, None)

	assert not result
