import os
import pytest
from chroma_feedback.provider.codeship.core import fetch, fetch_auth


def test_fetch_slug():
	if 'CODESHIP_USERNAME' in os.environ and 'CODESHIP_PASSWORD' in os.environ:
		result = []
		auth = fetch_auth('https://api.codeship.com', os.environ['CODESHIP_USERNAME'], os.environ['CODESHIP_PASSWORD'])

		for organization in auth['organizations']:
			result.extend(fetch('https://api.codeship.com', organization['uuid'], '372431', auth['token']))

		assert result[0]['provider'] == 'codeship'
		assert result[0]['slug'] == '372431'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('CODESHIP_USERNAME or CODESHIP_PASSWORD')


def test_fetch_user():
	if 'CODESHIP_USERNAME' in os.environ and 'CODESHIP_PASSWORD' in os.environ:
		result = []
		auth = fetch_auth('https://api.codeship.com', os.environ['CODESHIP_USERNAME'], os.environ['CODESHIP_PASSWORD'])

		for organization in auth['organizations']:
			result.extend(fetch('https://api.codeship.com', organization['uuid'], None, auth['token']))

		assert result[0]['provider'] == 'codeship'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('CODESHIP_USERNAME or CODESHIP_PASSWORD is not defined')


def test_fetch_invalid():
	result = fetch(None, None, None, None)

	assert result == []
