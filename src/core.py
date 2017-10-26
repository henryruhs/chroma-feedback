from __future__ import print_function
import sys
import os
import threading
import requests
import src.wording as wording
from openrazer.client import DeviceManager, DaemonNotFound


def init():
	try:
		device_manager = DeviceManager()
		device_manager.sync_effects = True
	except DaemonNotFound:
		print(wording.get('daemon_no') + wording.get('exclamation_mark'))
		exit(1)


def run(repository, interval):
	data = requests.get('https://api.travis-ci.org/repos/' + repository).json()
	status = 'passed'

	# handle data

	if len(data) == 0:
		sys.exit(1)
	if isinstance(data, dict):
		data = [data]

	# process data

	for item in data:
		if item['active'] is True:
			if item['last_build_status'] is None:
				print(wording.get('build_process').format(item['slug']))
				status = 'process'
			if item['last_build_status'] == 1:
				print(wording.get('build_failed').format(item['slug']))
				status = 'failed'

	# process device

	for device in device_manager.devices:
		if status == 'passed' and static(device, [0, 255, 0]):
			print(wording.get('setting_passed').format(device.name))
		if status == 'process' and static(device, [255, 255, 0]):
			print(wording.get('setting_process').format(device.name))
		if status == 'failed' and pulsate(device, [255, 0, 0]):
			print(wording.get('setting_failed').format(device.name))

	if interval > 0:
		threading.Timer(interval, run, args=[repository, interval]).start()


def static(device, rgb):
	if device.fx.has('logo') and device.fx.has('scroll'):
		return device.fx.misc.logo.static(rgb[0], rgb[1], rgb[2]) and device.fx.misc.scroll_wheel.static(rgb[0], rgb[1], rgb[2])
	return device.fx.static(rgb[0], rgb[1], rgb[2])


def pulsate(device, rgb):
	if device.fx.has('logo') and device.fx.has('scroll'):
		return device.fx.misc.logo.pulsate(rgb[0], rgb[1], rgb[2]) and device.fx.misc.scroll_wheel.pulsate(rgb[0], rgb[1], rgb[2])
	return device.fx.breath_single(rgb[0], rgb[1], rgb[2])


def destroy(number, frame):
	print('\r' + wording.get('goodbye') + wording.get('exclamation_mark'))
	os._exit(0)
