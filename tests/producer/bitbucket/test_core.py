import os
import pytest
from typing import get_args

from chroma_feedback.producer.bitbucket.core import fetch
from chroma_feedback.typing import Status


def test_fetch_slug() -> None:
	if os.environ.get('BITBUCKET_USERNAME') and os.environ.get('BITBUCKET_PASSWORD'):
		result = fetch('https://api.bitbucket.org', 'redaxmedia/chroma-feedback-test', os.environ.get('BITBUCKET_USERNAME'), os.environ.get('BITBUCKET_PASSWORD'))

		assert result[0]['name'] == 'bitbucket'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('BITBUCKET_USERNAME or BITBUCKET_PASSWORD is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert not result
