import pytest
import os
import argparse
from typing import get_args

from chroma_feedback.producer import github
from chroma_feedback.typing import Status


def test_run_one() -> None:
	if os.environ.get('GITHUB_TOKEN'):
		github.core.ARGS = argparse.Namespace(
			github_host = 'https://api.github.com',
			github_slug =
			[
				'redaxmedia/chroma-feedback'
			],
			github_token = os.environ.get('GITHUB_TOKEN')
		)
		result = github.core.run()

		assert result[0]['name'] == 'github'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert 'https://github.com/redaxmedia/chroma-feedback/actions/runs' in result[0]['url']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('GITHUB_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('GITHUB_TOKEN'):
		github.core.ARGS = argparse.Namespace(
			github_host = 'https://api.github.com',
			github_slug =
			[
				'redaxmedia'
			],
			github_token = os.environ.get('GITHUB_TOKEN')
		)
		result = github.core.run()

		assert result[0]['name'] == 'github'
		assert result[0]['slug']
		assert 'https://github.com/redaxmedia' in result[0]['url']
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'github'
		assert result[1]['slug']
		assert 'https://github.com/redaxmedia' in result[1]['url']
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('GITHUB_TOKEN is not defined')

