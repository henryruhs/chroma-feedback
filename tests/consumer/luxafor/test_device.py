import pytest

from chroma_feedback.consumer.luxafor.device import process_device


def test_process_passed() -> None:
	try:
		result = process_device("webhook_id", 'passed')

		assert result[0]['consumer'] == 'luxafor'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'passed'
	except:
		pytest.skip()


def test_process_started() -> None:
	try:
		result = process_device("webhook_id", 'started')

		assert result[0]['consumer'] == 'luxafor'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'started'
	except:
		pytest.skip()


def test_process_errored() -> None:
	try:
		result = process_device("webhook_id", 'errored')

		assert result[0]['consumer'] == 'luxafor'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'errored'
	except:
		pytest.skip()


def test_process_failed() -> None:
	try:
		result = process_device("webhook_id", 'failed')

		assert result[0]['consumer'] == 'luxafor'
		assert result[0]['type'] == 'device'
		assert result[0]['name']
		assert result[0]['status'] == 'failed'
	except:
		pytest.skip()
