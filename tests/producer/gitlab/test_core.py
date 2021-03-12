import os
import pytest
from chroma_feedback.producer.gitlab.core import fetch


def test_fetch_slug() -> None:
	if os.environ.get('GITLAB_TOKEN'):
		result = fetch('https://gitlab.com', '7311836', os.environ.get('GITLAB_TOKEN'))

		assert result[0]['producer'] == 'gitlab'
		assert result[0]['slug']
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('GITLAB_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert result == []
