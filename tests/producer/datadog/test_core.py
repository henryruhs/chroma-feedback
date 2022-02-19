import argparse
from typing import Any, get_args
from unittest.mock import patch

from chroma_feedback.producer import datadog
from chroma_feedback.typing import Status


@patch('requests.get')
def test_run_one(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'name': 'chroma-feedback',
		'overall_state': 'OK'
	}
	datadog.core.ARGS = argparse.Namespace(
		datadog_host = 'https://api.datadoghq.com',
		datadog_slug =
		[
			'1'
		],
		datadog_api_key = '__api_key__',
		datadog_application_key = '__application_key__'
	)
	result = datadog.core.run()

	assert result[0]['name'] == 'datadog'
	assert result[0]['slug'] == 'chroma-feedback'
	assert result[0]['status'] in get_args(Status)
