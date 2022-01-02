from typing import Any
from unittest.mock import patch
from chroma_feedback.producer.custom.core import fetch


@patch('requests.get')
def test_fetch_slug(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	[
		{
			'producer': 'custom',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	]
	result = fetch('https://localhost', 'redaxmedia/chroma-feedback')

	assert result[0]['producer'] == 'custom'
	assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert result[0]['active'] is True
	assert result[0]['status']


def test_fetch_invalid() -> None:
	result = fetch(None, None)

	assert not result
