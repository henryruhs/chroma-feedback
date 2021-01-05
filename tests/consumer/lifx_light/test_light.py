try:
	from unittest.mock import MagicMock
except ImportError:
	from mock import MagicMock
from chroma_feedback.consumer.lifx_light.light import process_lights

MOCK = MagicMock()


def test_process_passed() -> None:
	result = process_lights(
	{
		MOCK
	}, 'passed')

	assert result[0]['consumer'] == 'lifx_light'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'passed'


def test_process_started() -> None:
	result = process_lights(
	{
		MOCK
	}, 'started')

	assert result[0]['consumer'] == 'lifx_light'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'started'


def test_process_errored() -> None:
	result = process_lights(
	{
		MOCK
	}, 'errored')

	assert result[0]['consumer'] == 'lifx_light'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'errored'


def test_process_failed() -> None:
	result = process_lights(
	{
		MOCK
	}, 'failed')

	assert result[0]['consumer'] == 'lifx_light'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'failed'
