import os
import pytest
from chroma_feedback.provider.github.core import fetch

def test_fetch_slug():
	if 'GITHUB_TOKEN' in os.environ:
		result = fetch('https://api.github.com', 'redaxmedia/chroma-feedback', 'redaxmedia', os.environ['GITHUB_TOKEN'])

		assert result[0]['provider'] == 'github'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('GITHUB_TOKEN is not defined')


def test_fetch_invalid():
	result = fetch(None, None, None, None)

	assert result == []
