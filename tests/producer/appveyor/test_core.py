import os
import pytest
from chroma_feedback.producer.appveyor.core import fetch


def test_fetch_slug() -> None:
	result = fetch('https://ci.appveyor.com', 'redaxmedia/chroma-feedback', None)

	assert result[0]['producer'] == 'appveyor'
	assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert result[0]['active'] is True
	assert result[0]['status']


def test_fetch_user() -> None:
	if 'APPVEYOR_TOKEN' in os.environ:
		result = fetch('https://ci.appveyor.com', None, os.environ['APPVEYOR_TOKEN'])

		assert result[0]['producer'] == 'appveyor'
		assert result[0]['slug']
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('APPVEYOR_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert result == []
