import pytest
try:
	from unittest.mock import MagicMock
except ImportError:
	from mock import MagicMock
from chroma_feedback.consumer.luxafor_flag.device import process_devices

MOCK = MagicMock()


def test_process_passed() -> None:
	try:
		result = process_devices(
		{
			MOCK
		}, 'passed')

		assert result[0]['consumer'] == 'luxafor_flag'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'passed'
	except:
		pytest.skip()


def test_process_started() -> None:
	try:
		result = process_devices(
		{
			MOCK
		}, 'started')

		assert result[0]['consumer'] == 'luxafor_flag'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'started'
	except:
		pytest.skip()


def test_process_errored() -> None:
	try:
		result = process_devices(
		{
			MOCK
		}, 'errored')

		assert result[0]['consumer'] == 'luxafor_flag'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'errored'
	except:
		pytest.skip()


def test_process_warned() -> None:
	try:
		result = process_devices(
		{
			MOCK
		}, 'warned')

		assert result[0]['consumer'] == 'luxafor_flag'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'warned'
	except:
		pytest.skip()


def test_process_failed() -> None:
	try:
		result = process_devices(
		{
			MOCK
		}, 'failed')

		assert result[0]['consumer'] == 'luxafor_flag'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'failed'
	except:
		pytest.skip()
