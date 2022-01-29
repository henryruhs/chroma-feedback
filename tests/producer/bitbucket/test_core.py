import os
import pytest
from chroma_feedback.producer.bitbucket.core import fetch


def test_fetch_slug() -> None:
	if os.environ.get('BITBUCKET_USERNAME') and os.environ.get('BITBUCKET_PASSWORD'):
		result = fetch('https://api.bitbucket.org', 'redaxmedia/test-dummy', os.environ.get('BITBUCKET_USERNAME'), os.environ.get('BITBUCKET_PASSWORD'))

		assert result[0]['producer'] == 'bitbucket'
		assert result[0]['slug'] == 'redaxmedia/test-dummy'
		assert result[0]['status']
	else:
		pytest.skip('BITBUCKET_USERNAME or CODESHIP_PASSWORD is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert not result
