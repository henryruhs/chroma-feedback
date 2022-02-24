import pytest
import os
import argparse
from typing import get_args

from chroma_feedback.producer import buddy
from chroma_feedback.typing import Status


def test_run_one() -> None:
	if os.environ.get('BUDDY_TOKEN'):
		buddy.core.ARGS = argparse.Namespace(
			buddy_host = 'https://api.buddy.works',
			buddy_slug =
			[
				'redaxmedia/chroma-feedback-test-gitlab'
			],
			buddy_token = os.environ.get('BUDDY_TOKEN')
		)
		result = buddy.core.run()

		assert result[0]['name'] == 'buddy'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback-test-gitlab'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('BUDDY_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('BUDDY_TOKEN'):
		buddy.core.ARGS = argparse.Namespace(
			buddy_host = 'https://api.buddy.works',
			buddy_slug =
			[
				'redaxmedia'
			],
			buddy_token = os.environ.get('BUDDY_TOKEN')
		)
		result = buddy.core.run()

		assert result[0]['name'] == 'buddy'
		assert 'redaxmedia/chroma-feedback-test' in result[0]['slug']
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'buddy'
		assert 'redaxmedia/chroma-feedback-test' in result[1]['slug']
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('BUDDY_TOKEN is not defined')
