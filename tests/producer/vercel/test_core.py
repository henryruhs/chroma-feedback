import os
import pytest
from typing import get_args

from chroma_feedback.producer.vercel.core import fetch
from chroma_feedback.typing import Status


def test_fetch_slug() -> None:
	if os.environ.get('VERCEL_TOKEN'):
		result = fetch('https://api.vercel.com', 'chroma-feedback-test-gitlab', os.environ.get('VERCEL_TOKEN'))

		assert result[0]['name'] == 'vercel'
		assert result[0]['slug'] == 'chroma-feedback-test-gitlab'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('VERCEL_TOKEN is not defined')


def test_fetch_user() -> None:
	if os.environ.get('VERCEL_TOKEN'):
		result = fetch('https://api.vercel.com', None, os.environ.get('VERCEL_TOKEN'))

		assert result[0]['name'] == 'vercel'
		assert result[0]['slug'] == 'chroma-feedback-test-gitlab'
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'vercel'
		assert result[1]['slug'] == 'chroma-feedback-test-bitbucket'
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('VERCEL_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
