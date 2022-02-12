import os
import pytest
from typing import get_args

from chroma_feedback.producer.heroku.core import fetch
from chroma_feedback.typing import Status


def test_fetch_slug() -> None:
	if os.environ.get('HEROKU_TOKEN'):
		result = fetch('https://api.heroku.com', 'chroma-feedback-test', os.environ.get('HEROKU_TOKEN'))

		assert result[0]['name'] == 'heroku'
		assert result[0]['slug'] == 'chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('HEROKU_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
