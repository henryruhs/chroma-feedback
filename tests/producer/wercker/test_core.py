import os
import pytest
from chroma_feedback.producer.wercker.core import fetch


def test_fetch_slug() -> None:
	if 'WERCKER_TOKEN' in os.environ:
		result = fetch('https://app.wercker.com', 'redaxmedia/chroma-feedback', os.environ['WERCKER_TOKEN'])

		assert result[0]['producer'] == 'wercker'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('WERCKER_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert result == []
