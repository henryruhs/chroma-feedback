import os
import pytest
from src.provider import circle


def test_fetch_slug():
	result = circle.fetch('https://circleci.com', 'github/redaxmedia/chroma-feedback', None)

	assert result[0]['provider'] == 'circle'
	assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert result[0]['active'] is True
	assert result[0]['status']


def test_fetch_token():
	if 'CIRCLE_TOKEN' in os.environ:
		result = circle.fetch('https://circleci.com', None, os.environ['CIRCLE_TOKEN'])

		assert result[0]['provider'] == 'circle'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('CIRCLE_TOKEN not defined')


def test_fetch_invalid():
	result = circle.fetch(None, None, None)

	assert result == []
