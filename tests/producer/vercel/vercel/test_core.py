import argparse
import os
from typing import get_args

import pytest

from chroma_feedback.producer.vercel import vercel
from chroma_feedback.types import Status


def test_run_one() -> None:
	if os.environ.get('VERCEL_TOKEN'):
		vercel.core.ARGS = argparse.Namespace(
			vercel_host = 'https://api.vercel.com',
			vercel_slug =
			[
				'chroma-feedback-test-gitlab'
			],
			vercel_token = os.environ.get('VERCEL_TOKEN')
		)
		result = vercel.core.run()

		assert result[0]['name'] == 'vercel'
		assert result[0]['slug'] == 'chroma-feedback-test-gitlab'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('VERCEL_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('VERCEL_TOKEN'):
		vercel.core.ARGS = argparse.Namespace(
			vercel_host = 'https://api.vercel.com',
			vercel_slug = None,
			vercel_token = os.environ.get('VERCEL_TOKEN')
		)
		result = vercel.core.run()

		assert result[0]['name'] == 'vercel'
		assert result[0]['slug']
		assert result[0]['status'] in get_args(Status)

		assert result[1]['name'] == 'vercel'
		assert result[1]['slug']
		assert result[1]['status'] in get_args(Status)
	else:
		pytest.skip('VERCEL_TOKEN is not defined')
