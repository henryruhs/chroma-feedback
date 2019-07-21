from mock import MagicMock
from chroma_feedback.consumer.thingm_blink.device import process_devices

mock = MagicMock()
devices =\
{
	mock
}


def test_process_passed():
	result = process_devices('passed', devices)

	assert result[0]['consumer'] == 'thingm_blink'
	assert result[0]['type'] == 'device'
	assert result[0]['name']
	assert result[0]['status'] == 'passed'


def test_process_process():
	result = process_devices('process', devices)

	assert result[0]['consumer'] == 'thingm_blink'
	assert result[0]['type'] == 'device'
	assert result[0]['name']
	assert result[0]['status'] == 'process'


def test_process_errored():
	result = process_devices('errored', devices)

	assert result[0]['consumer'] == 'thingm_blink'
	assert result[0]['type'] == 'device'
	assert result[0]['name']
	assert result[0]['status'] == 'errored'


def test_process_failed():
	result = process_devices('failed', devices)

	assert result[0]['consumer'] == 'thingm_blink'
	assert result[0]['type'] == 'device'
	assert result[0]['name']
	assert result[0]['status'] == 'failed'
