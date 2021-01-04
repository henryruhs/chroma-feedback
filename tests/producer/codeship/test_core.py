import os
import pytest
from chroma_feedback.producer.codeship.core import fetch


def test_fetch_slug() -> None:
	if 'CODESHIP_USERNAME' in os.environ and 'CODESHIP_PASSWORD' in os.environ:
		result = fetch('https://api.codeship.com', 'redaxmedia/chroma-feedback', os.environ['CODESHIP_USERNAME'], os.environ['CODESHIP_PASSWORD'])

		assert result[0]['producer'] == 'codeship'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('CODESHIP_USERNAME or CODESHIP_PASSWORD')


def test_fetch_user() -> None:
	if 'CODESHIP_USERNAME' in os.environ and 'CODESHIP_PASSWORD' in os.environ:
		result = fetch('https://api.codeship.com', None, os.environ['CODESHIP_USERNAME'], os.environ['CODESHIP_PASSWORD'])

		assert result[0]['producer'] == 'codeship'
		assert result[0]['slug']
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('CODESHIP_USERNAME or CODESHIP_PASSWORD is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert result == []
