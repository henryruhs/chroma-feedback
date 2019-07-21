from mock import MagicMock
from chroma_feedback.consumer.philips_hue.light import process_lights

mock = MagicMock()
lights =\
{
	mock
}


def test_process_passed():
	result = process_lights('passed', lights)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'passed'


def test_process_process():
	result = process_lights('process', lights)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'process'


def test_process_errored():
	result = process_lights('errored', lights)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'errored'


def test_process_failed():
	result = process_lights('failed', lights)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['type'] == 'light'
	assert result[0]['name']
	assert result[0]['status'] == 'failed'
