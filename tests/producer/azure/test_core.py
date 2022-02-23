import argparse
from typing import Any, get_args
from unittest.mock import patch

from chroma_feedback.producer import azure
from chroma_feedback.typing import Status


@patch('requests.get')
def test_run_one(request_mock : Any) -> None:
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
	azure.core.ARGS = argparse.Namespace(
		azure_host = 'https://dev.azure.com',
		azure_slug =
		[
			'redaxmedia/chroma-feedback'
		],
		azure_token = '__token__'
	)
	result = azure.run()

	assert result[0]['name'] == 'azure' 
	assert result[0]['slug'] == 'chroma-feedback'
	assert result[0]['status'] in get_args(Status)
