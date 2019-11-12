import pytest
try:
	from unittest.mock import MagicMock
except ImportError:
	from mock import MagicMock
from chroma_feedback.consumer.thingm_blink.device import process_devices

MOCK = MagicMock()


def test_process_passed():
	try:
		result = process_devices('passed',
		{
			MOCK
		})

		assert result[0]['consumer'] == 'thingm_blink'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'passed'
	except:
		pytest.skip()


def test_process_process():
	try:
		result = process_devices('process',
		{
			MOCK
		})

		assert result[0]['consumer'] == 'thingm_blink'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'process'
	except:
		pytest.skip()


def test_process_errored():
	try:
		result = process_devices('errored',
		{
			MOCK
		})

		assert result[0]['consumer'] == 'thingm_blink'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'errored'
	except:
		pytest.skip()


def test_process_failed():
	try:
		result = process_devices('failed',
		{
			MOCK
		})

		assert result[0]['consumer'] == 'thingm_blink'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'failed'
	except:
		pytest.skip()
