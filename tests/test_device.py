from unittest.mock import MagicMock
import src.device as device

mock = MagicMock()
mock.name = 'Razer Chroma'
mock =\
[
	mock
]


def test_process_device_passed():
	data = device.process_device(mock, 'passed')
	assert 'Setting Razer Chroma to build passed' in data['message'][0]
	assert data['status'] == 'passed'


def test_process_device_process():
	data = device.process_device(mock, 'process')
	assert 'Setting Razer Chroma to build in process' in data['message'][0]
	assert data['status'] == 'process'


def test_process_device_errored():
	data = device.process_device(mock, 'errored')
	assert 'Setting Razer Chroma to build errored' in data['message'][0]
	assert data['status'] == 'errored'


def test_process_device_failed():
	data = device.process_device(mock, 'failed')
	assert 'Setting Razer Chroma to build failed' in data['message'][0]
	assert data['status'] == 'failed'
