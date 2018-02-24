import os
import pytest
from src.provider import circle


def test_fetch_slug():
	data = circle.fetch('github/redaxmedia/chroma-feedback', None)
	assert data[0]['provider'] == 'circle'
	assert data[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert data[0]['active'] is True
	assert data[0]['status']


def test_fetch_user():
	if 'CIRCLE_TOKEN' in os.environ:
		data = circle.fetch(None, os.environ['CIRCLE_TOKEN'])
		assert data[0]['provider'] == 'circle'
		assert data[0]['active'] is True
		assert data[0]['status']
	else:
		pytest.skip('CIRCLE_TOKEN not defined')
