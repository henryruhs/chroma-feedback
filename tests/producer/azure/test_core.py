from typing import Any, get_args
from unittest.mock import patch
from chroma_feedback.typing import Status
from chroma_feedback.producer.azure.core import fetch


@patch('requests.get')
def test_fetch_slug(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'value':
		[
			{
				'status': 'completed',
				'result': 'succeeded',
				'project':
				{
					'name': 'chroma-feedback'
				}
			}
		]
	}
	result = fetch('https://dev.azure.com', 'redaxmedia/chroma-feedback', '__token__')

	assert result[0]['name'] == 'azure'
	assert result[0]['slug'] == 'chroma-feedback'
	assert result[0]['status'] in get_args(Status)


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
