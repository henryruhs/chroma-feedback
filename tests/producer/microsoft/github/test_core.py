import argparse
import os
from typing import get_args

import pytest

from chroma_feedback.producer.microsoft import github
from chroma_feedback.typing import Status


def test_run_one() -> None:
	if os.environ.get('MICROSOFT_GITHUB_TOKEN'):
		github.core.ARGS = argparse.Namespace(
			microsoft_github_host = 'https://api.github.com',
			microsoft_github_slug =
			[
				'henryruhs/chroma-feedback'
			],
			microsoft_github_token = os.environ.get('MICROSOFT_GITHUB_TOKEN')
		)
		result = github.core.run()

		assert result[0]['name'] == 'microsoft.github'
		assert result[0]['slug'] == 'henryruhs/chroma-feedback'
		assert 'https://github.com/henryruhs/chroma-feedback/actions/runs' in result[0]['url']
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('MICROSOFT_GITHUB_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('MICROSOFT_GITHUB_TOKEN'):
		github.core.ARGS = argparse.Namespace(
			microsoft_github_host = 'https://api.github.com',
			microsoft_github_slug =
			[
				'henryruhs'
			],
			microsoft_github_token = os.environ.get('MICROSOFT_GITHUB_TOKEN')
		)
		result = github.core.run()

		assert result[0]['name'] == 'microsoft.github'
		assert result[0]['slug']
		assert 'https://github.com/henryruhs' in result[0]['url']
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'microsoft.github'
		assert result[1]['slug']
		assert 'https://github.com/henryruhs' in result[1]['url']
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('MICROSOFT_GITHUB_TOKEN is not defined')

