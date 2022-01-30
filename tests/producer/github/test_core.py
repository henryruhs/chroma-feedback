from typing import get_args
import os
import pytest
from chroma_feedback.typing import Status
from chroma_feedback.producer.github.core import fetch


def test_fetch_slug() -> None:
	if os.environ.get('GITHUB_TOKEN'):
		result = fetch('https://api.github.com', 'redaxmedia/chroma-feedback', os.environ.get('GITHUB_TOKEN'))

		assert result[0]['name'] == 'github'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('GITHUB_TOKEN is not defined')


def test_fetch_user() -> None:
	if os.environ.get('GITHUB_TOKEN'):
		result = fetch('https://api.github.com', 'redaxmedia', os.environ.get('GITHUB_TOKEN'))

		assert result[0]['name'] == 'github'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('GITHUB_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
