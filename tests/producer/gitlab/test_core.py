from typing import get_args
import os
import pytest
from chroma_feedback.typing import Status
from chroma_feedback.producer.gitlab.core import fetch


def test_fetch_slug() -> None:
	if os.environ.get('GITLAB_TOKEN'):
		result = fetch('https://gitlab.com', '7311836', os.environ.get('GITLAB_TOKEN'))

		assert result[0]['producer'] == 'gitlab'
		assert result[0]['slug']
		assert 'https://gitlab.com/redaxmedia/test-dummy' in result[0]['url']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('GITLAB_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
