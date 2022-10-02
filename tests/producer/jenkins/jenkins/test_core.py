import argparse
from typing import Any, get_args
from unittest.mock import patch

from chroma_feedback.producer.jenkins import jenkins
from chroma_feedback.typing import Status


@patch('requests.get')
def test_run_one(request_mock : Any) -> None:
	request_mock.return_value.status_code = 200
	request_mock.return_value.json.return_value =\
	{
		'building': False,
		'result': 'SUCCESS'
	}
	jenkins.core.ARGS = argparse.Namespace(
		jenkins_host = 'http://localhost',
		jenkins_slug =
		[
			'chroma-feedback'
		],
		jenkins_username = '__username__',
		jenkins_token = '__token__'
	)
	result = jenkins.run()

	assert result[0]['name'] == 'jenkins'
	assert result[0]['slug'] == 'chroma-feedback'
	assert result[0]['status'] in get_args(Status)
