from mock import MagicMock
from src.consumer import philips_hue

mock = MagicMock()
mock.name = 'Philips Hue'
groups =\
{
	1: mock
}


def test_process_passed():
	result = philips_hue.process('passed', groups)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'passed'


def test_process_process():
	result = philips_hue.process('process', groups)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'process'


def test_process_errored():
	result = philips_hue.process('errored', groups)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'errored'


def test_process_failed():
	result = philips_hue.process('failed', groups)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'failed'
