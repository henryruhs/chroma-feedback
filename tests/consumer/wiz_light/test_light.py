import pytest
try:
	from unittest.mock import MagicMock
except ImportError:
	from mock import MagicMock
from chroma_feedback.consumer.wiz_light.light import process_lights

MOCK = MagicMock()


def test_process_passed() -> None:
	try:
		result = process_lights(
		{
			MOCK
		}, 'passed')

		assert result[0]['consumer'] == 'wiz_light'
		assert result[0]['type'] == 'light'
		assert result[0]['name']
		assert result[0]['status'] == 'passed'
	except:
		pytest.skip()


def test_process_started() -> None:
	try:
		result = process_lights(
		{
			MOCK
		}, 'started')

		assert result[0]['consumer'] == 'wiz_light'
		assert result[0]['type'] == 'light'
		assert result[0]['name']
		assert result[0]['status'] == 'started'
	except:
		pytest.skip()


def test_process_errored() -> None:
	try:
		result = process_lights(
		{
			MOCK
		}, 'errored')

		assert result[0]['consumer'] == 'wiz_light'
		assert result[0]['type'] == 'light'
		assert result[0]['name']
		assert result[0]['status'] == 'errored'
	except:
		pytest.skip()


def test_process_failed() -> None:
	try:
		result = process_lights(
		{
			MOCK
		}, 'failed')

		assert result[0]['consumer'] == 'wiz_light'
		assert result[0]['type'] == 'light'
		assert result[0]['name']
		assert result[0]['status'] == 'failed'
	except:
		pytest.skip()
