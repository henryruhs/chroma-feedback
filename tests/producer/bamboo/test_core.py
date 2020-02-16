import os
import pytest
from chroma_feedback.producer.bamboo.core import fetch


def test_fetch_project_slug() -> None:
	if 'BAMBOO_HOST' in os.environ and 'BAMBOO_PROJECT_SLUG' in os.environ and 'BAMBOO_USERNAME' in os.environ and 'BAMBOO_TOKEN' in os.environ:
		result = fetch(os.environ['BAMBOO_HOST'], os.environ['BAMBOO_PROJECT_SLUG'], os.environ['BAMBOO_USERNAME'], os.environ['BAMBOO_TOKEN'])

		assert result[0]['producer'] == 'bamboo'
		assert result[0]['slug']
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('BAMBOO_HOST and BAMBOO_PROJECT_SLUG and BAMBOO_USERNAME and BAMBOO_TOKEN must be defined.')


def test_fetch_plan_slug() -> None:
	if 'BAMBOO_HOST' in os.environ and 'BAMBOO_PLAN_SLUG' in os.environ and 'BAMBOO_USERNAME' in os.environ and 'BAMBOO_TOKEN' in os.environ:
		result = fetch(os.environ['BAMBOO_HOST'], os.environ['BAMBOO_PLAN_SLUG'], os.environ['BAMBOO_USERNAME'], os.environ['BAMBOO_TOKEN'])

		assert result[0]['producer'] == 'bamboo'
		assert result[0]['slug']
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('BAMBOO_HOST and BAMBOO_PLAN_SLUG and BAMBOO_USERNAME and BAMBOO_TOKEN must be defined.')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert result == []
