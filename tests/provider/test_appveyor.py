import os
import pytest
from src.provider import appveyor


def test_fetch_slug():
	data = appveyor.fetch(None, 'redaxmedia/chroma-feedback', None)
	assert data[0]['provider'] == 'appveyor'
	assert data[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert data[0]['active'] is True
	assert data[0]['status']


def test_fetch_user():
	if 'APPVEYOR_TOKEN' in os.environ:
		data = appveyor.fetch(None, None, os.environ['APPVEYOR_TOKEN'])
		assert data[0]['provider'] == 'appveyor'
		assert data[0]['active'] is True
		assert data[0]['status']
	else:
		pytest.skip('APPVEYOR_TOKEN not defined')
