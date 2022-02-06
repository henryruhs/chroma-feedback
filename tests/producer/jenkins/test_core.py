from typing import Any, get_args
from unittest.mock import patch

from chroma_feedback.producer.jenkins.core import fetch
from chroma_feedback.typing import Status


@patch('requests.get')
def test_fetch_slug(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'building': False,
		'result': 'SUCCESS'
	}
	result = fetch('https://localhost', 'chroma-feedback', '__username__', '__password__')

	assert result[0]['name'] == 'jenkins'
	assert result[0]['slug'] == 'chroma-feedback'
	assert result[0]['status'] in get_args(Status)


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert not result
