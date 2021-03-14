import os
import pytest
from chroma_feedback.consumer.luxafor.device import process_devices


def test_process_passed() -> None:
	if os.environ.get('LUXAFOR_ID'):
		result = process_devices('https://api.luxafor.com',
		[
			os.environ.get('LUXAFOR_ID')
		], 'passed')

		assert result[0]['consumer'] == 'luxafor'
		assert result[0]['type'] == 'device'
		assert result[0]['name'] == os.environ.get('LUXAFOR_ID')
		assert result[0]['status'] == 'passed'
	else:
		pytest.skip('LUXAFOR_ID is not defined')


def test_process_started() -> None:
	if os.environ.get('LUXAFOR_ID'):
		result = process_devices('https://api.luxafor.com',
		[
			os.environ.get('LUXAFOR_ID')
		], 'started')

		assert result[0]['consumer'] == 'luxafor'
		assert result[0]['type'] == 'device'
		assert result[0]['name'] == os.environ.get('LUXAFOR_ID')
		assert result[0]['status'] == 'started'
	else:
		pytest.skip('LUXAFOR_ID is not defined')


def test_process_errored() -> None:
	if os.environ.get('LUXAFOR_ID'):
		result = process_devices('https://api.luxafor.com',
		 [
			 os.environ.get('LUXAFOR_ID')
		 ], 'errored')

		assert result[0]['consumer'] == 'luxafor'
		assert result[0]['type'] == 'device'
		assert result[0]['name'] == os.environ.get('LUXAFOR_ID')
		assert result[0]['status'] == 'errored'
	else:
		pytest.skip('LUXAFOR_ID is not defined')


def test_process_failed() -> None:
	if os.environ.get('LUXAFOR_ID'):
		result = process_devices('https://api.luxafor.com',
		[
			os.environ.get('LUXAFOR_ID')
		], 'failed')

		assert result[0]['consumer'] == 'luxafor'
		assert result[0]['type'] == 'device'
		assert result[0]['name'] == os.environ.get('LUXAFOR_ID')
		assert result[0]['status'] == 'failed'
	else:
		pytest.skip('LUXAFOR_ID is not defined')
