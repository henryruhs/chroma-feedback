import os
import pytest
from chroma_feedback.producer.circle.core import fetch


def test_fetch_slug() -> None:
	if 'CIRCLE_TOKEN' in os.environ:
		result = fetch('https://circleci.com', None, 'github/redaxmedia/chroma-feedback', os.environ['CIRCLE_TOKEN'])

		assert result[0]['producer'] == 'circle'
		assert result[0]['slug'] == 'gh/redaxmedia/chroma-feedback/lint-and-test'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('CIRCLE_TOKEN is not defined')


def test_fetch_organization() -> None:
	if 'CIRCLE_TOKEN' in os.environ:
		result = fetch('https://circleci.com', 'github/redaxmedia', None, os.environ['CIRCLE_TOKEN'])

		assert result[0]['producer'] == 'circle'
		assert result[0]['slug']
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('CIRCLE_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert result == []
