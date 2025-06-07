import os
from typing import get_args

import pytest

from chroma_feedback.producer.heroku import heroku
from chroma_feedback.types import Status


def test_run_one() -> None:
	if os.environ.get('HEROKU_TOKEN'):
		heroku.core.ARGS =\
		{
			'heroku_host': 'https://api.heroku.com',
			'heroku_slug':
			[
				'chroma-feedback-test'
			],
			'heroku_token': os.environ.get('HEROKU_TOKEN')
		}
		result = heroku.core.run()

		assert result[0]['name'] == 'heroku'
		assert result[0]['slug'] == 'chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('HEROKU_TOKEN is not defined')


def test_run_many() -> None:
	if os.environ.get('HEROKU_TOKEN'):
		heroku.core.ARGS =\
		{
			'heroku_host': 'https://api.heroku.com',
			'heroku_slug': None,
			'heroku_token': os.environ.get('HEROKU_TOKEN')
		}
		result = heroku.core.run()

		assert result[0]['name'] == 'heroku'
		assert result[0]['slug'] == 'chroma-feedback-test'
		assert result[0]['status'] in get_args(Status)
	else:
		pytest.skip('HEROKU_TOKEN is not defined')
