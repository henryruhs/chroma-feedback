import os
from typing import get_args

import pytest

from chroma_feedback.producer.netlify import netlify
from chroma_feedback.types import Status


def test_run_one() -> None:
	if os.environ.get('NETLIFY_TOKEN'):
		netlify.core.ARGS =\
		{
			'netlify_host': 'https://api.netlify.com',
			'netlify_slug':
			[
				'b31e0317-4398-4545-80fc-811ecc997a6e'
			],
			'netlify_token': os.environ.get('NETLIFY_TOKEN')
		}
		result = netlify.core.run()

		assert result[0]['name'] == 'netlify'
		assert result[0]['slug'] == 'chroma-feedback-test-gitlab'
		assert 'https://app.netlify.com/projects/chroma-feedback-test-gitlab' in result[0]['url']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('NETLIFY_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('NETLIFY_TOKEN'):
		netlify.core.ARGS =\
		{
			'netlify_host': 'https://api.netlify.com',
			'netlify_slug': None,
			'netlify_token': os.environ.get('NETLIFY_TOKEN')
		}
		result = netlify.core.run()

		assert result[0]['name'] == 'netlify'
		assert result[0]['slug'] == 'chroma-feedback-test-bitbucket'
		assert 'https://app.netlify.com/projects/chroma-feedback-test-bitbucket' in result[0]['url']
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'netlify'
		assert result[1]['slug'] == 'chroma-feedback-test-gitlab'
		assert 'https://app.netlify.com/projects/chroma-feedback-test-gitlab' in result[1]['url']
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('NETLIFY_TOKEN is not defined')
