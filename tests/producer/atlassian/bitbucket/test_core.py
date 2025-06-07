import os
from typing import get_args

import pytest

from chroma_feedback.producer.atlassian import bitbucket
from chroma_feedback.types import Status


def test_run_one() -> None:
	if os.environ.get('ATLASSIAN_BITBUCKET_USERNAME') and os.environ.get('ATLASSIAN_BITBUCKET_PASSWORD'):
		bitbucket.core.ARGS =\
		{
			'atlassian_bitbucket_host': 'https://api.bitbucket.org',
			'atlassian_bitbucket_slug':
			[
				'henryruhs/chroma-feedback-test'
			],
			'atlassian_bitbucket_username': os.environ.get('ATLASSIAN_BITBUCKET_USERNAME'),
			'atlassian_bitbucket_password': os.environ.get('ATLASSIAN_BITBUCKET_PASSWORD')
		}
		result = bitbucket.core.run()

		assert result[0]['name'] == 'atlassian.bitbucket'
		assert result[0]['slug'] == 'henryruhs/chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('ATLASSIAN_BITBUCKET_USERNAME or ATLASSIAN_BITBUCKET_PASSWORD is not defined')
