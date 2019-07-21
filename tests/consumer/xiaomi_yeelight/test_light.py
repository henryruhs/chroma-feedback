from mock import MagicMock
from chroma_feedback.consumer.xiaomi_yeelight.light import process_lights

MOCK = MagicMock()


def test_process_passed():
	result = process_lights('passed',
	{
		MOCK
	})

	assert result[0]['consumer'] == 'xiaomi_yeelight'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'passed'


def test_process_process():
	result = process_lights('process',
	{
		MOCK
	})

	assert result[0]['consumer'] == 'xiaomi_yeelight'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'process'


def test_process_errored():
	result = process_lights('errored',
	{
		MOCK
	})

	assert result[0]['consumer'] == 'xiaomi_yeelight'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'errored'


def test_process_failed():
	result = process_lights('failed',
	{
		MOCK
	})

	assert result[0]['consumer'] == 'xiaomi_yeelight'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'failed'
