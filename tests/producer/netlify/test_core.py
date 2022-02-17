import pytest
import os
import argparse
from typing import get_args

from chroma_feedback.producer import netlify
from chroma_feedback.typing import Status


def test_core_one() -> None:
	if os.environ.get('NETLIFY_TOKEN'):
		netlify.core.ARGS = argparse.Namespace(
			netlify_host = 'https://api.netlify.com',
			netlify_slug =
			[
				'0b9627b8-da58-4dfc-8056-9645c02dcab6'
			],
			netlify_token = os.environ.get('NETLIFY_TOKEN')
		)
		result = netlify.core.run()

		assert result[0]['name'] == 'netlify'
		assert result[0]['slug'] == 'chroma-feedback-test-gitlab'
		assert 'https://app.netlify.com/sites/chroma-feedback-test-gitlab' in result[0]['url']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('NETLIFY_TOKEN is not defined')


def test_core_many() -> None:
	if os.environ.get('NETLIFY_TOKEN'):
		netlify.core.ARGS = argparse.Namespace(
			netlify_host = 'https://api.netlify.com',
			netlify_slug = None,
			netlify_token = os.environ.get('NETLIFY_TOKEN')
		)
		result = netlify.core.run()

		assert result[0]['name'] == 'netlify'
		assert result[0]['slug'] == 'chroma-feedback-test-bitbucket'
		assert 'https://app.netlify.com/sites/chroma-feedback-test-bitbucket' in result[0]['url']
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'netlify'
		assert result[1]['slug'] == 'chroma-feedback-test-gitlab'
		assert 'https://app.netlify.com/sites/chroma-feedback-test-gitlab' in result[1]['url']
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('NETLIFY_TOKEN is not defined')
