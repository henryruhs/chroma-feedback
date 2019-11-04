import os
import pytest
from chroma_feedback.provider.codeship.core import fetch, fetch_token


def test_fetch_project():
	if 'CODESHIP_USERNAME' in os.environ and 'CODESHIP_PASSWORD' in os.environ and 'CODESHIP_ORGANIZATION' in os.environ and 'CODESHIP_PROJECT' in os.environ:
		token = fetch_token('https://api.codeship.com', os.environ['CODESHIP_USERNAME'], os.environ['CODESHIP_PASSWORD'])
		result = fetch('https://api.codeship.com', os.environ['CODESHIP_ORGANIZATION'], os.environ['CODESHIP_PROJECT'], token)

		assert result[0]['provider'] == 'codeship'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('CODESHIP_USERNAME or CODESHIP_PASSWORD or CODESHIP_ORGANIZATION or CODESHIP_PROJECT is not defined')


def test_fetch_invalid():
	result = fetch(None, None, None, None)

	assert result == []
