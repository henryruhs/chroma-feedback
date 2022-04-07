import pytest
import os
import argparse
from typing import get_args

from chroma_feedback.producer import bitbucket
from chroma_feedback.typing import Status


def test_run_one() -> None:
	if os.environ.get('BITBUCKET_USERNAME') and os.environ.get('BITBUCKET_PASSWORD'):
		bitbucket.core.ARGS = argparse.Namespace(
			bitbucket_host = 'https://api.bitbucket.org',
			bitbucket_slug =
			[
				'henryruhs/chroma-feedback-test'
			],
			bitbucket_username = os.environ.get('BITBUCKET_USERNAME'),
			bitbucket_password = os.environ.get('BITBUCKET_PASSWORD')
		)
		result = bitbucket.core.run()

		assert result[0]['name'] == 'bitbucket'
		assert result[0]['slug'] == 'henryruhs/chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('BITBUCKET_USERNAME or BITBUCKET_PASSWORD is not defined')
