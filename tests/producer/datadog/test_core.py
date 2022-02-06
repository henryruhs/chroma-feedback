from typing import Any, get_args
from unittest.mock import patch

from chroma_feedback.producer.datadog.core import fetch
from chroma_feedback.typing import Status


@patch('requests.get')
def test_fetch_slug(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'name': 'chroma-feedback',
		'overall_state': 'OK'
	}
	result = fetch('https://api.datadoghq.com', '1', '__api_key__', '__application_key__')

	assert result[0]['name'] == 'datadog'
	assert result[0]['slug'] == 'chroma-feedback'
	assert result[0]['status'] in get_args(Status)


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert not result
