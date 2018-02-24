from mock import MagicMock
from src import device

mock = MagicMock()
mock.name = 'Razer Chroma'
mock =\
[
	mock
]


def test_process_passed():
	data = device.process(mock, 'passed')
	assert 'Setting Razer Chroma to build passed' in data['message'][0]
	assert data['status'] == 'passed'


def test_process_process():
	data = device.process(mock, 'process')
	assert 'Setting Razer Chroma to build in process' in data['message'][0]
	assert data['status'] == 'process'


def test_process_errored():
	data = device.process(mock, 'errored')
	assert 'Setting Razer Chroma to build errored' in data['message'][0]
	assert data['status'] == 'errored'


def test_process_failed():
	data = device.process(mock, 'failed')
	assert 'Setting Razer Chroma to build failed' in data['message'][0]
	assert data['status'] == 'failed'
