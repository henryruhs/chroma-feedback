from mock import MagicMock
from chroma_feedback.consumer import lifx_light

mock = MagicMock()
lights =\
{
	mock
}


def test_process_lights_passed():
	result = lifx_light.process_lights('passed', lights)

	assert result[0]['consumer'] == 'lifx_light'
	assert result[0]['name']
	assert result[0]['status'] == 'passed'


def test_process_lights_process():
	result = lifx_light.process_lights('process', lights)

	assert result[0]['consumer'] == 'lifx_light'
	assert result[0]['name']
	assert result[0]['status'] == 'process'


def test_process_lights_errored():
	result = lifx_light.process_lights('errored', lights)

	assert result[0]['consumer'] == 'lifx_light'
	assert result[0]['name']
	assert result[0]['status'] == 'errored'


def test_process_lights_failed():
	result = lifx_light.process_lights('failed', lights)

	assert result[0]['consumer'] == 'lifx_light'
	assert result[0]['name']
	assert result[0]['status'] == 'failed'
