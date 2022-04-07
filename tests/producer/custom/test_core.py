import argparse
from typing import Any, get_args
from unittest.mock import patch

from chroma_feedback.producer import custom
from chroma_feedback.typing import Status


@patch('requests.get')
def test_run_one(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	[
		{
			'producer': 'custom',
			'slug': 'henryruhs/chroma-feedback',
			'url': 'http://localhost/henryruhs/chroma-feedback/pipelines/1',
			'status': 'passed'
		}
	]
	custom.core.ARGS = argparse.Namespace(
		custom_host = 'http://localhost',
		custom_slug =
		[
			'henryruhs/chroma-feedback'
		],
		custom_token = '__token__'
	)
	result = custom.core.run()

	assert result[0]['name'] == 'custom'
	assert result[0]['slug'] == 'henryruhs/chroma-feedback'
	assert result[0]['url'] == 'http://localhost/henryruhs/chroma-feedback/pipelines/1'
	assert result[0]['status'] in get_args(Status)
