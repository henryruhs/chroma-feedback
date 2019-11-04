import os
import pytest
from chroma_feedback.provider.gitlab.core import fetch


def test_fetch_slug():
	if 'GITLAB_TOKEN' in os.environ:
		result = fetch('https://gitlab.com', '7311836', os.environ['GITLAB_TOKEN'])

		assert result[0]['provider'] == 'gitlab'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('GITLAB_TOKEN is not defined')


def test_fetch_invalid():
	result = fetch(None, None, None)

	assert result == []
