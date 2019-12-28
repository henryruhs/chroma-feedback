import os
import pytest
from chroma_feedback.producer.github.core import fetch

def test_fetch_slug() -> None:
	if 'GITHUB_TOKEN' in os.environ:
		result = fetch('https://api.github.com', 'redaxmedia/chroma-feedback', 'redaxmedia', os.environ['GITHUB_TOKEN'])

		assert result[0]['producer'] == 'github'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('GITHUB_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert result == []
