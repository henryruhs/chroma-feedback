from mock import MagicMock
from chroma_feedback.consumer import xiaomi_yeelight

mock = MagicMock()
devices =\
[
	mock
]


def test_process_passed():
	result = xiaomi_yeelight.process('passed', devices)

	assert result[0]['consumer'] == 'xiaomi_yeelight'
	assert result[0]['name']
	assert result[0]['status'] == 'passed'


def test_process_process():
	result = xiaomi_yeelight.process('process', devices)

	assert result[0]['consumer'] == 'xiaomi_yeelight'
	assert result[0]['name']
	assert result[0]['status'] == 'process'


def test_process_errored():
	result = xiaomi_yeelight.process('errored', devices)

	assert result[0]['consumer'] == 'xiaomi_yeelight'
	assert result[0]['name']
	assert result[0]['status'] == 'errored'


def test_process_failed():
	result = xiaomi_yeelight.process('failed', devices)

	assert result[0]['consumer'] == 'xiaomi_yeelight'
	assert result[0]['name']
	assert result[0]['status'] == 'failed'
