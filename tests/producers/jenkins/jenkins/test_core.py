from typing import Any, get_args
from unittest.mock import patch

from chroma_feedback.producers.jenkins import jenkins
from chroma_feedback.types import Status


@patch('requests.get')
def test_run_one(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'building': False,
		'result': 'SUCCESS'
	}
	jenkins.core.ARGS =\
	{
		'jenkins_host': '__host__',
		'jenkins_slug':
		[
			'chroma-feedback'
		],
		'jenkins_username': '__username__',
		'jenkins_token': '__token__'
	}
	result = jenkins.run()

	assert result[0]['name'] == 'jenkins'
	assert result[0]['slug'] == 'chroma-feedback'
	assert result[0]['status'] in get_args(Status)
