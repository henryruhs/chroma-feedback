from mock import MagicMock
from src.consumer import razer_chroma

mock = MagicMock()
mock.name = 'Razer Chroma'
mock =\
[
	mock
]


def test_process_passed():
	provider_result = razer_chroma.process('passed', mock)

	assert 'Setting Razer Chroma to build passed' in provider_result['message'][0]


def test_process_process():
	provider_result = razer_chroma.process('process', mock)

	assert 'Setting Razer Chroma to build in process' in provider_result['message'][0]


def test_process_errored():
	provider_result = razer_chroma.process('errored', mock)

	assert 'Setting Razer Chroma to build errored' in provider_result['message'][0]


def test_process_failed():
	provider_result = razer_chroma.process('failed', mock)

	assert 'Setting Razer Chroma to build failed' in provider_result['message'][0]
