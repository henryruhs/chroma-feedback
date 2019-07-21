import pytest
from mock import MagicMock
from chroma_feedback.consumer.philips_hue.light import process_lights

MOCK = MagicMock()


def test_process_passed():
	try:
		result = process_lights('passed',
		{
			MOCK
		})

		assert result[0]['consumer'] == 'philips_hue'
		assert result[0]['type'] == 'light'
		assert result[0]['name']
		assert result[0]['status'] == 'passed'
	except SystemExit:
		pytest.skip()


def test_process_process():
	try:
		result = process_lights('process',
		{
			MOCK
		})

		assert result[0]['consumer'] == 'philips_hue'
		assert result[0]['type'] == 'light'
		assert result[0]['name']
		assert result[0]['status'] == 'process'
	except SystemExit:
		pytest.skip()


def test_process_errored():
	try:
		result = process_lights('errored',
		{
			MOCK
		})

		assert result[0]['consumer'] == 'philips_hue'
		assert result[0]['type'] == 'light'
		assert result[0]['name']
		assert result[0]['status'] == 'errored'
	except SystemExit:
		pytest.skip()


def test_process_failed():
	try:
		result = process_lights('failed',
		{
			MOCK
		})

		assert result[0]['consumer'] == 'philips_hue'
		assert result[0]['type'] == 'light'
		assert result[0]['name']
		assert result[0]['status'] == 'failed'
	except SystemExit:
		pytest.skip()
