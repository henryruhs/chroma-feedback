import os
import pytest
from chroma_feedback.producer.bitbucket.core import fetch


def test_fetch_slug() -> None:
	if 'BITBUCKET_USERNAME' in os.environ and 'BITBUCKET_PASSWORD' in os.environ:
		result = fetch('https://api.bitbucket.org', 'redaxmedia/test-dummy', os.environ['BITBUCKET_USERNAME'], os.environ['BITBUCKET_PASSWORD'])

		assert result[0]['producer'] == 'bitbucket'
		assert result[0]['slug'] == 'redaxmedia/test-dummy'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('BITBUCKET_USERNAME or CODESHIP_PASSWORD')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert result == []
