import sys
import threading
import requests

from openrazer.client import DeviceManager

device_manager = DeviceManager()
device_manager.sync_effects = True


def run(repository, interval):
	data = requests.get('https://api.travis-ci.org/repos/' + repository).json()
	status = 'passed'

	# handle data

	if len(data) == 0:
		sys.exit(1)
	if type(data) == dict:
		data = [data]

	# process data

	for item in data:
		if item['active'] is True:
			if item['last_build_status'] is None:
				print('Build of {} in process'.format(item['slug']))
				status = 'process'
			if item['last_build_status'] == 1:
				print('Build of {} failed'.format(item['slug']))
				status = 'failed'

	# process device

	for device in device_manager.devices:
		if status == 'passed' and static(device, [0, 255, 0]):
			print('Setting {} to build passed'.format(device.name))
		if status == 'process' and static(device, [255, 255, 255]):
			print('Setting {} to build in process'.format(device.name))
		if status == 'failed' and breath_single(device, [255, 0, 0]):
			print('Setting {} to build failed'.format(device.name))

	if interval > 0:
		threading.Timer(interval, run, args=[repository, interval]).start()


def static(device, rgb):
	if device.fx.has('logo') and device.fx.has('scroll'):
		return device.fx.misc.logo.static(rgb[0], rgb[1], rgb[2]) and device.fx.misc.scroll_wheel.static(rgb[0], rgb[1], rgb[2])
	else:
		return device.fx.static(rgb[0], rgb[1], rgb[2])


def breath_single(device, rgb):
	if device.fx.has('logo') and device.fx.has('scroll'):
		return device.fx.misc.logo.breath_single(rgb[0], rgb[1], rgb[2]) and device.fx.misc.scroll_wheel.breath_single(rgb[0], rgb[1], rgb[2])
	else:
		return device.fx.breath_single(rgb[0], rgb[1], rgb[2])
