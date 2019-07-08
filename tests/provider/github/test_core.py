import os
import pytest
from src.provider import github

def test_fetch_slug():
	if 'GITHUB_PASSWORD' in os.environ:
		result = github.fetch('https://api.github.com', 'redaxmedia/chroma-feedback', 'redaxmedia', os.environ['GITHUB_PASSWORD'])

		assert result[0]['provider'] == 'github'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('GITHUB_PASSWORD not defined')


def test_fetch_invalid():
	result = github.fetch(None, None, None, None)

	assert result == []
