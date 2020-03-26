from typing import Any
from unittest.mock import patch
from chroma_feedback.producer.jenkins.core import fetch


@patch('requests.get')
def test_fetch_slug(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'building': False,
		'result': 'SUCCESS'
	}
	result = fetch('https://localhost', 'chroma-feedback', None, None)

	assert result[0]['producer'] == 'jenkins'
	assert result[0]['slug'] == 'chroma-feedback'
	assert result[0]['active'] is True
	assert result[0]['status']


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert result == []
