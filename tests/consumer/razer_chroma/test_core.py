from mock import MagicMock
from src.consumer import razer_chroma

mock = MagicMock()
mock.name = 'Razer Chroma'
mock =\
[
	mock
]


def test_process_passed():
	provider_result = razer_chroma.process(mock, 'passed')
	assert 'Setting Razer Chroma to build passed' in provider_result['message'][0]
	assert provider_result['status'] == 'passed'


def test_process_process():
	provider_result = razer_chroma.process(mock, 'process')
	assert 'Setting Razer Chroma to build in process' in provider_result['message'][0]
	assert provider_result['status'] == 'process'


def test_process_errored():
	provider_result = razer_chroma.process(mock, 'errored')
	assert 'Setting Razer Chroma to build errored' in provider_result['message'][0]
	assert provider_result['status'] == 'errored'


def test_process_failed():
	provider_result = razer_chroma.process(mock, 'failed')
	assert 'Setting Razer Chroma to build failed' in provider_result['message'][0]
	assert provider_result['status'] == 'failed'
