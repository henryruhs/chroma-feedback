import pytest
import os
import argparse
from typing import get_args

from chroma_feedback.producer.cloudbees import codeship
from chroma_feedback.typing import Status


def test_run_one() -> None:
	if os.environ.get('CLOUDBEES_CODESHIP_USERNAME') and os.environ.get('CLOUDBEES_CODESHIP_PASSWORD'):
		codeship.core.ARGS = argparse.Namespace(
			cloudbees_codeship_host = 'https://api.codeship.com',
			cloudbees_codeship_slug =
			[
				'henryruhs/chroma-feedback-test'
			],
			cloudbees_codeship_username = os.environ.get('CLOUDBEES_CODESHIP_USERNAME'),
			cloudbees_codeship_password = os.environ.get('CLOUDBEES_CODESHIP_PASSWORD')
		)
		result = codeship.core.run()

		assert result[0]['name'] == 'cloudbees.codeship'
		assert result[0]['slug'] == 'henryruhs/chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('CLOUDBEES_CODESHIP_USERNAME or CLOUDBEES_CODESHIP_PASSWORD is not defined')


def test_run_many() -> None:
	if os.environ.get('CLOUDBEES_CODESHIP_USERNAME') and os.environ.get('CLOUDBEES_CODESHIP_PASSWORD'):
		codeship.core.ARGS = argparse.Namespace(
			cloudbees_codeship_host = 'https://api.codeship.com',
			cloudbees_codeship_slug = None,
			cloudbees_codeship_username = os.environ.get('CLOUDBEES_CODESHIP_USERNAME'),
			cloudbees_codeship_password = os.environ.get('CLOUDBEES_CODESHIP_PASSWORD')
		)
		result = codeship.core.run()

		assert result[0]['name'] == 'cloudbees.codeship'
		assert result[0]['slug'] == 'henryruhs/chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'cloudbees.codeship'
		assert result[1]['slug'] == 'henryruhs/chroma-feedback-test'
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('CLOUDBEES_CODESHIP_USERNAME or CLOUDBEES_CODESHIP_PASSWORD is not defined')
