import os
import pytest
import src.provider.circle.core as circle


def test_fetch_slug():
	result = circle.fetch(None, 'github/redaxmedia/chroma-feedback', None)
	assert result[0]['provider'] == 'circle'
	assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert result[0]['active'] is True
	assert result[0]['status']


def test_fetch_user():
	if 'CIRCLE_TOKEN' in os.environ:
		result = circle.fetch(None, None, os.environ['CIRCLE_TOKEN'])
		assert result[0]['provider'] == 'circle'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('CIRCLE_TOKEN not defined')


def test_fetch_invalid():
	result = circle.fetch(None, None, None)
	assert result == []
