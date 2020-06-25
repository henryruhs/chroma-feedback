import os
import pytest
from chroma_feedback.producer.codeship.core import fetch, fetch_auth


def test_fetch_slug() -> None:
	if 'CODESHIP_USERNAME' in os.environ and 'CODESHIP_PASSWORD' in os.environ:
		result = []
		auth = fetch_auth('https://api.codeship.com', os.environ['CODESHIP_USERNAME'], os.environ['CODESHIP_PASSWORD'])

		if 'organizations' in auth:
			for organization in auth['organizations']:
				result.extend(fetch('https://api.codeship.com', organization['uuid'], '372431', auth['token']))
		else:
			pytest.skip('AUTHENTICATION FAILED')

		assert result[0]['producer'] == 'codeship'
		assert result[0]['slug'] == '372431'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('CODESHIP_USERNAME or CODESHIP_PASSWORD')


def test_fetch_user() -> None:
	if 'CODESHIP_USERNAME' in os.environ and 'CODESHIP_PASSWORD' in os.environ:
		result = []
		auth = fetch_auth('https://api.codeship.com', os.environ['CODESHIP_USERNAME'], os.environ['CODESHIP_PASSWORD'])

		if 'organizations' in auth:
			for organization in auth['organizations']:
				result.extend(fetch('https://api.codeship.com', organization['uuid'], None, auth['token']))
		else:
			pytest.skip('AUTHENTICATION FAILED')

		assert result[0]['producer'] == 'codeship'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('CODESHIP_USERNAME or CODESHIP_PASSWORD is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert result == []
