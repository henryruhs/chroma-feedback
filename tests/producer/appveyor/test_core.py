from typing import get_args
import os
import pytest
from chroma_feedback.typing import Status
from chroma_feedback.producer.appveyor.core import fetch


def test_fetch_slug() -> None:
	if os.environ.get('APPVEYOR_TOKEN'):
		result = fetch('https://ci.appveyor.com', 'redaxmedia/chroma-feedback', os.environ.get('APPVEYOR_TOKEN'))

		assert result[0]['producer'] == 'appveyor'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('APPVEYOR_TOKEN is not defined')


def test_fetch_user() -> None:
	if os.environ.get('APPVEYOR_TOKEN'):
		result = fetch('https://ci.appveyor.com', None, os.environ.get('APPVEYOR_TOKEN'))

		assert result[0]['producer'] == 'appveyor'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('APPVEYOR_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
