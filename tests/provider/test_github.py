import os
import pytest
from src.provider import github


def test_fetch_slug():
	if 'GITHUB_TOKEN' in os.environ:
		data = github.fetch(None, 'redaxmedia/chroma-feedback', os.environ['GITHUB_TOKEN'])
		assert data[0]['provider'] == 'github'
		assert data[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert data[0]['active'] is True
		assert data[0]['status']
	else:
		pytest.skip('GITHUB_TOKEN not defined')


def test_fetch_invalid():
	data = github.fetch(None, None, None)
	assert data == []
