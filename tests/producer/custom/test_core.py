from typing import Any, get_args
from unittest.mock import patch

from chroma_feedback.producer.custom.core import fetch
from chroma_feedback.typing import Status


@patch('requests.get')
def test_fetch_slug(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	[
		{
			'producer': 'custom',
			'slug': 'redaxmedia/chroma-feedback',
			'url': 'https://localhost/redaxmedia/chroma-feedback/pipelines/1',
			'status': 'passed'
		}
	]
	result = fetch('https://localhost', 'redaxmedia/chroma-feedback')

	assert result[0]['name'] == 'custom'
	assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert result[0]['url'] == 'https://localhost/redaxmedia/chroma-feedback/pipelines/1'
	assert result[0]['status'] in get_args(Status)


def test_fetch_invalid() -> None:
	result = fetch(None, None)

	assert not result
