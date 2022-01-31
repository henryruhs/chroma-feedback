from typing import Any, get_args
from unittest.mock import patch
from chroma_feedback.typing import Status
from chroma_feedback.producer.bamboo.core import fetch


@patch('requests.get')
def test_fetch_plan_slug(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'key': 'redaxmedia-chroma_feedback',
		'buildState': 'Successful'
	}
	result = fetch('http://localhost', 'redaxmedia-chroma_feedback', '__token__')

	assert result[0]['name'] == 'bamboo'
	assert result[0]['slug'] == 'redaxmedia-chroma_feedback'
	assert result[0]['status'] in get_args(Status)


@patch('requests.get')
def test_fetch_project_slug(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'results':
		{
			'result':
			[
				{
					'key': 'redaxmedia-chroma_feedback',
					'buildState': 'Successful'
				}
			]
		}
	}
	result = fetch('http://localhost', 'redaxmedia', '__token__')

	assert result[0]['name'] == 'bamboo'
	assert result[0]['slug'] == 'redaxmedia-chroma_feedback'
	assert result[0]['status'] in get_args(Status)


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
