import os
import pytest
from chroma_feedback.producer.buddy.core import fetch


def test_fetch_slug() -> None:
	if os.environ.get('BUDDY_TOKEN'):
		result = fetch('https://api.buddy.works', 'redaxmedia-clone/chroma-feedback', os.environ.get('BUDDY_TOKEN'))

		assert result[0]['producer'] == 'buddy'
		assert result[0]['slug'] == 'redaxmedia-clone/chroma-feedback'
		assert result[0]['status']
	else:
		pytest.skip('BUDDY_TOKEN is not defined')


def test_fetch_organization() -> None:
	if os.environ.get('BUDDY_TOKEN'):
		result = fetch('https://api.buddy.works', 'redaxmedia-clone', os.environ.get('BUDDY_TOKEN'))

		assert result[0]['producer'] == 'buddy'
		assert result[0]['slug']
		assert result[0]['status']
	else:
		pytest.skip('BUDDY_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
