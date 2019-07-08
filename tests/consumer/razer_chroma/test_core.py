from mock import MagicMock
from src.consumer import razer_chroma

mock = MagicMock()
mock.name = 'Razer Chroma'
mock =\
[
	mock
]


def test_process_passed():
	result = razer_chroma.process('passed', mock)

	assert result[0]['consumer'] == 'razer_chroma'
	assert result[0]['name'] == 'Razer Chroma'
	assert result[0]['active']
	assert result[0]['status'] == 'passed'


def test_process_process():
	result = razer_chroma.process('process', mock)

	assert result[0]['consumer'] == 'razer_chroma'
	assert result[0]['name'] == 'Razer Chroma'
	assert result[0]['active']
	assert result[0]['status'] == 'process'


def test_process_errored():
	result = razer_chroma.process('errored', mock)

	assert result[0]['consumer'] == 'razer_chroma'
	assert result[0]['name'] == 'Razer Chroma'
	assert result[0]['active']
	assert result[0]['status'] == 'errored'


def test_process_failed():
	result = razer_chroma.process('failed', mock)

	assert result[0]['consumer'] == 'razer_chroma'
	assert result[0]['name'] == 'Razer Chroma'
	assert result[0]['active']
	assert result[0]['status'] == 'failed'
