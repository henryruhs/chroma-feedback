import os
import pytest
from typing import get_args

from chroma_feedback.producer.netlify.core import fetch
from chroma_feedback.typing import Status


def test_fetch_slug() -> None:
	if os.environ.get('NETLIFY_TOKEN'):
		result = fetch('https://api.netlify.com', '0b9627b8-da58-4dfc-8056-9645c02dcab6', os.environ.get('NETLIFY_TOKEN'))

		assert result[0]['name'] == 'netlify'
		assert result[0]['slug'] == 'chroma-feedback-test-gitlab'
		assert 'https://app.netlify.com/sites/chroma-feedback-test-gitlab' in result[0]['url']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('NETLIFY_TOKEN is not defined')


def test_fetch_user() -> None:
	if os.environ.get('NETLIFY_TOKEN'):
		result = fetch('https://api.netlify.com', None, os.environ.get('NETLIFY_TOKEN'))

		assert result[0]['name'] == 'netlify'
		assert result[0]['slug'] == 'chroma-feedback-test-bitbucket'
		assert 'https://app.netlify.com/sites/chroma-feedback-test-bitbucket' in result[0]['url']
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'netlify'
		assert result[1]['slug'] == 'chroma-feedback-test-gitlab'
		assert 'https://app.netlify.com/sites/chroma-feedback-test-gitlab' in result[1]['url']
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('NETLIFY_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
