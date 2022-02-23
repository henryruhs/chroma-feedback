import pytest
import os
import argparse
from typing import get_args

from chroma_feedback.producer import codeship
from chroma_feedback.typing import Status


def test_run_one() -> None:
	if os.environ.get('CODESHIP_USERNAME') and os.environ.get('CODESHIP_PASSWORD'):
		codeship.core.ARGS = argparse.Namespace(
			codeship_host = 'https://api.codeship.com',
			codeship_slug =
			[
				'redaxmedia/chroma-feedback-test'
			],
			codeship_username = os.environ.get('CODESHIP_USERNAME'),
			codeship_password = os.environ.get('CODESHIP_PASSWORD')
		)
		result = codeship.core.run()

		assert result[0]['name'] == 'codeship'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('CODESHIP_USERNAME or CODESHIP_PASSWORD is not defined')


def test_run_many() -> None:
	if os.environ.get('CODESHIP_USERNAME') and os.environ.get('CODESHIP_PASSWORD'):
		codeship.core.ARGS = argparse.Namespace(
			codeship_host = 'https://api.codeship.com',
			codeship_slug = None,
			codeship_username = os.environ.get('CODESHIP_USERNAME'),
			codeship_password = os.environ.get('CODESHIP_PASSWORD')
		)
		result = codeship.core.run()

		assert result[0]['name'] == 'codeship'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'codeship'
		assert result[1]['slug'] == 'redaxmedia/chroma-feedback-test'
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('CODESHIP_USERNAME or CODESHIP_PASSWORD is not defined')
