from typing import Any
from unittest.mock import patch
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
	result = fetch('https://dev.azure.com', 'redaxmedia/chroma-feedback', 'token')

	assert result[0]['producer'] == 'azure'
	assert result[0]['slug'] == 'chroma-feedback'
	assert result[0]['status']


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
