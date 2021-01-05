try:
	from unittest.mock import MagicMock
except ImportError:
	from mock import MagicMock
from chroma_feedback.consumer.agile_innovative_blinkstick.device import process_devices

MOCK = MagicMock()


def test_process_passed() -> None:
	result = process_devices(
	{
		MOCK
	}, 'passed')

	assert result[0]['consumer'] == 'agile_innovative_blinkstick'
	assert result[0]['type'] == 'device'
	assert result[0]['name']
	assert result[0]['status'] == 'passed'


def test_process_started() -> None:
	result = process_devices(
	{
		MOCK
	}, 'started')

	assert result[0]['consumer'] == 'agile_innovative_blinkstick'
	assert result[0]['type'] == 'device'
	assert result[0]['name']
	assert result[0]['status'] == 'started'


def test_process_errored() -> None:
	result = process_devices(
	{
		MOCK
	}, 'errored')

	assert result[0]['consumer'] == 'agile_innovative_blinkstick'
	assert result[0]['type'] == 'device'
	assert result[0]['name']
	assert result[0]['status'] == 'errored'


def test_process_failed() -> None:
	result = process_devices(
	{
		MOCK
	}, 'failed')

	assert result[0]['consumer'] == 'agile_innovative_blinkstick'
	assert result[0]['type'] == 'device'
	assert result[0]['name']
	assert result[0]['status'] == 'failed'
