from mock import MagicMock
from src.consumer import thingm_blink

mock = MagicMock()
devices =\
{
	mock
}


def test_process_passed():
	result = thingm_blink.process('passed', devices)

	assert result[0]['consumer'] == 'thingm_blink'
	assert result[0]['name']
	assert result[0]['status'] == 'passed'


def test_process_process():
	result = thingm_blink.process('process', devices)

	assert result[0]['consumer'] == 'thingm_blink'
	assert result[0]['name']
	assert result[0]['status'] == 'process'


def test_process_errored():
	result = thingm_blink.process('errored', devices)

	assert result[0]['consumer'] == 'thingm_blink'
	assert result[0]['name']
	assert result[0]['status'] == 'errored'


def test_process_failed():
	result = thingm_blink.process('failed', devices)

	assert result[0]['consumer'] == 'thingm_blink'
	assert result[0]['name']
	assert result[0]['status'] == 'failed'
