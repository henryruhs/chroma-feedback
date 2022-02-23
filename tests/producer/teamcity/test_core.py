import argparse
from typing import Any, get_args
from unittest.mock import patch

from chroma_feedback.producer import teamcity
from chroma_feedback.typing import Status


@patch('requests.get')
def test_run_one(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'buildType':
		[
			{
				'builds':
				{
					'build':
					[
						{
							'status': 'SUCCESS',
							'running': False,
							'buildType':
							{
								'projectName': 'chroma-feedback',
								'paused': False
							}
						}
					]
				}
			}
		]
	}
	teamcity.core.ARGS = argparse.Namespace(
		teamcity_host = 'http://localhost',
		teamcity_slug =
		[
			'chroma-feedback'
		],
		teamcity_token = '__token__'
	)
	result = teamcity.run()

	assert result[0]['name'] == 'teamcity'
	assert result[0]['slug'] == 'chroma-feedback'
	assert result[0]['status'] in get_args(Status)
