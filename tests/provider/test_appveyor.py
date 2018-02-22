import os
import pytest
from src.provider import appveyor


def test_fetch_data_slug():
	data = appveyor.fetch_data('redaxmedia/redaxscript', None)
	assert len(data) == 1


def test_fetch_data_user():
	if 'APPVEYOR_TOKEN' in os.environ:
		token = os.environ['APPVEYOR_TOKEN']
		data = appveyor.fetch_data(None, token)
		assert len(data) > 0
	else:
		pytest.skip('APPVEYOR_TOKEN not defined')
