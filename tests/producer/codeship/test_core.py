from typing import get_args
import os
import pytest
from chroma_feedback.typing import Status
from chroma_feedback.producer.codeship.core import fetch


def test_fetch_slug() -> None:
	if os.environ.get('CODESHIP_USERNAME') and os.environ.get('CODESHIP_PASSWORD'):
		result = fetch('https://api.codeship.com', 'redaxmedia/chroma-feedback', os.environ.get('CODESHIP_USERNAME'), os.environ.get('CODESHIP_PASSWORD'))

		assert result[0]['name'] == 'codeship'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('CODESHIP_USERNAME or CODESHIP_PASSWORD is not defined')


def test_fetch_user() -> None:
	if os.environ.get('CODESHIP_USERNAME') and os.environ.get('CODESHIP_PASSWORD'):
		result = fetch('https://api.codeship.com', None, os.environ.get('CODESHIP_USERNAME'), os.environ.get('CODESHIP_PASSWORD'))

		assert result[0]['name'] == 'codeship'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('CODESHIP_USERNAME or CODESHIP_PASSWORD is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert not result
