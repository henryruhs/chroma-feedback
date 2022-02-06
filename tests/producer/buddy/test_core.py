import os
import pytest
from typing import get_args

from chroma_feedback.producer.buddy.core import fetch
from chroma_feedback.typing import Status


def test_fetch_slug() -> None:
	if os.environ.get('BUDDY_TOKEN'):
		result = fetch('https://api.buddy.works', 'redaxmedia/chroma-feedback', os.environ.get('BUDDY_TOKEN'))

		assert result[0]['name'] == 'buddy'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('BUDDY_TOKEN is not defined')


def test_fetch_organization() -> None:
	if os.environ.get('BUDDY_TOKEN'):
		result = fetch('https://api.buddy.works', 'redaxmedia', os.environ.get('BUDDY_TOKEN'))

		assert result[0]['name'] == 'buddy'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('BUDDY_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
