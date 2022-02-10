import os
import pytest
from typing import get_args

from chroma_feedback.producer.netlify.core import fetch
from chroma_feedback.typing import Status


def test_fetch_slug() -> None:
	if os.environ.get('NETLIFY_TOKEN'):
		result = fetch('https://api.netlify.com', 'db187aa3-c68e-4264-bfe6-c3fc92ee0582', os.environ.get('NETLIFY_TOKEN'))

		assert result[0]['name'] == 'netlify'
		assert result[0]['slug'] == 'epic-davinci-8e7fbd'
		assert 'https://app.netlify.com/sites/epic-davinci-8e7fbd' in result[0]['url']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('NETLIFY_TOKEN is not defined')


def test_fetch_user() -> None:
	if os.environ.get('NETLIFY_TOKEN'):
		result = fetch('https://api.netlify.com', None, os.environ.get('NETLIFY_TOKEN'))

		assert result[0]['name'] == 'netlify'
		assert result[0]['slug'] == 'cranky-haibt-a0fa06'
		assert 'https://app.netlify.com/sites/cranky-haibt-a0fa06' in result[0]['url']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('NETLIFY_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
