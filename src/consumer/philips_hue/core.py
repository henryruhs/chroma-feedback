import json
import requests
from src import wording


def run(status):
	devices =\
	[
		'1',
		'2',
		'3',
		'4',
		'5',
		'6',
		'7'
	]

	# process

	return process(devices, status)


def process(devices, status):
	message = []

	# process devices

	for device in devices:
		if status == 'passed' and static(device, 25500):
			message.append(wording.get('setting_passed').format(device) + wording.get('point'))
		if status == 'process' and static(device, 17000):
			message.append(wording.get('setting_process').format(device) + wording.get('point'))
		if status == 'errored' and pulsate(device, 34000):
			message.append(wording.get('setting_errored').format(device) + wording.get('point'))
		if status == 'failed' and pulsate(device, 0):
			message.append(wording.get('setting_failed').format(device) + wording.get('point'))
	return\
	{
		'message': message,
		'status': status
	}


def static(light, hue):
	return update('http://192.168.1.29', '6a-VvQRmiOp9rZk7jWnk8MMfBJTm8BUzUHPUjybl', light,
	{
		'hue': hue,
		'on': True,
		'bri': 255,
		'alert': 'none'
	})


def pulsate(light, hue):
	return update('http://192.168.1.29', '6a-VvQRmiOp9rZk7jWnk8MMfBJTm8BUzUHPUjybl', light,
	 {
		'hue': hue,
		'on': True,
		'bri': 255,
		'alert': 'lselect'
	})


def update(host, user, light, data):
	response = None
	if host and user:
		response = requests.put(host + '/api/' + user + '/lights/' + light + '/state', data = json.dumps(data))

	# process response

	return response.status_code == 200
