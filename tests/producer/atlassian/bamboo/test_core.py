import argparse
from typing import Any, get_args
from unittest.mock import patch

from chroma_feedback.producer.atlassian import bamboo
from chroma_feedback.types import Status


@patch('requests.get')
def test_run_one(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'key': 'henryruhs-chroma-feedback',
		'buildState': 'Successful'
	}
	bamboo.core.ARGS = argparse.Namespace(
		atlassian_bamboo_host = 'http://localhost',
		atlassian_bamboo_slug =
		[
			'henryruhs/chroma-feedback'
		],
		atlassian_bamboo_token = '__token__'
	)
	result = bamboo.run()

	assert result[0]['name'] == 'atlassian.bamboo'
	assert result[0]['slug'] == 'henryruhs-chroma-feedback'
	assert result[0]['status'] in get_args(Status)


@patch('requests.get')
def test_run_many(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'results':
		{
			'result':
			[
				{
					'key': 'henryruhs-chroma-feedback',
					'buildState': 'Successful'
				}
			]
		}
	}
	bamboo.core.ARGS = argparse.Namespace(
		atlassian_bamboo_host = 'http://localhost',
		atlassian_bamboo_slug =
		[
			'henryruhs'
		],
		atlassian_bamboo_token = '__token__'
	)
	result = bamboo.run()

	assert result[0]['name'] == 'atlassian.bamboo'
	assert result[0]['slug'] == 'henryruhs-chroma-feedback'
	assert result[0]['status'] in get_args(Status)
