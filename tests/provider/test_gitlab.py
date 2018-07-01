import os
import pytest
from src.provider import gitlab


def test_fetch_user():
	if 'GITLAB_TOKEN' in os.environ:
		data = gitlab.fetch(None, '7311836', os.environ['GITLAB_TOKEN'])
		assert data[0]['provider'] == 'gitlab'
		assert data[0]['active'] is True
		assert data[0]['status']
	else:
		pytest.skip('GITLAB_TOKEN not defined')


def test_fetch_invalid():
	data = gitlab.fetch(None, None, None)
	assert data == []
