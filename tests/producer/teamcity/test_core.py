from typing import Any, get_args
from unittest.mock import patch

from chroma_feedback.producer.teamcity.core import fetch
from chroma_feedback.typing import Status


@patch('requests.get')
def test_fetch_slug(request_mock : Any) -> None:
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
	result = fetch('https://localhost', 'chroma-feedback', '__token__')

	assert result[0]['name'] == 'teamcity'
	assert result[0]['slug'] == 'chroma-feedback'
	assert result[0]['status'] in get_args(Status)


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert not result
