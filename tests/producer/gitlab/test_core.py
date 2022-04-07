import pytest
import os
import argparse
from typing import get_args

from chroma_feedback.producer import gitlab
from chroma_feedback.typing import Status


def test_run_one() -> None:
	if os.environ.get('GITLAB_TOKEN'):
		gitlab.core.ARGS = argparse.Namespace(
			gitlab_host = 'https://gitlab.com',
			gitlab_slug =
			[
				'33658238'
			],
			gitlab_token = os.environ.get('GITLAB_TOKEN')
		)
		result = gitlab.core.run()

		assert result[0]['name'] == 'gitlab'
		assert result[0]['slug'] == '33658238/test'
		assert 'https://gitlab.com/henryruhs/chroma-feedback-test' in result[0]['url']
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'gitlab'
		assert result[1]['slug'] == '33658238/lint'
		assert 'https://gitlab.com/henryruhs/chroma-feedback-test' in result[1]['url']
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('GITLAB_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('GITLAB_TOKEN'):
		gitlab.core.ARGS = argparse.Namespace(
			gitlab_host = 'https://gitlab.com',
			gitlab_slug = None,
			gitlab_token = os.environ.get('GITLAB_TOKEN')
		)
		result = gitlab.core.run()

		assert result[0]['name'] == 'gitlab'
		assert result[0]['slug'] == '33658238/test'
		assert 'https://gitlab.com/henryruhs/chroma-feedback-test' in result[0]['url']
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'gitlab'
		assert result[1]['slug'] == '33658238/lint'
		assert 'https://gitlab.com/henryruhs/chroma-feedback-test' in result[1]['url']
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('GITLAB_TOKEN is not defined')
