from mock import MagicMock
from chroma_feedback.consumer import philips_hue

mock = MagicMock()
lights =\
{
	mock
}
groups =\
{
	1: mock
}


def test_process_lights_passed():
	result = philips_hue.process_lights('passed', lights)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'passed'


def test_process_lights_process():
	result = philips_hue.process_lights('process', lights)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'process'


def test_process_lights_errored():
	result = philips_hue.process_lights('errored', lights)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'errored'


def test_process_lights_failed():
	result = philips_hue.process_lights('failed', lights)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'failed'


def test_process_groups_passed():
	result = philips_hue.process_groups('passed', groups)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'passed'


def test_process_groups_process():
	result = philips_hue.process_groups('process', groups)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'process'


def test_process_groups_errored():
	result = philips_hue.process_groups('errored', groups)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'errored'


def test_process_groups_failed():
	result = philips_hue.process_groups('failed', groups)

	assert result[0]['consumer'] == 'philips_hue'
	assert result[0]['name']
	assert result[0]['status'] == 'failed'
