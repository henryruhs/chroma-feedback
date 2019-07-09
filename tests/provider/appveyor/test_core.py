import os
import pytest
from src.provider import appveyor


def test_fetch_slug():
	result = appveyor.fetch('https://ci.appveyor.com', 'redaxmedia/chroma-feedback', None)

	assert result[0]['provider'] == 'appveyor'
	assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert result[0]['active'] is True
	assert result[0]['status']


def test_fetch_user():
	if 'APPVEYOR_TOKEN' in os.environ:
		result = appveyor.fetch('https://ci.appveyor.com', None, os.environ['APPVEYOR_TOKEN'])

		assert result[0]['provider'] == 'appveyor'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('APPVEYOR_TOKEN not defined')


def test_fetch_invalid():
	result = appveyor.fetch(None, None, None)

	assert result == []
