import os
import pytest
from src.provider import circle


def test_fetch_data_slug():
	data = circle.fetch_data('github/redaxmedia/chroma-feedback', None)
	assert len(data) == 1


def test_fetch_data_user():
	if 'CIRCLE_TOKEN' in os.environ:
		data = circle.fetch_data(None, os.environ['CIRCLE_TOKEN'])
		assert len(data) > 0
	else:
		pytest.skip('CIRCLE_TOKEN not defined')
