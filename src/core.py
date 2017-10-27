from __future__ import print_function
import sys
import os
import threading
import requests
import src.color as color
import src.wording as wording

try:
	from openrazer.client import DeviceManager, DaemonNotFound
except ImportError:
	print(wording.get('driver_no') + wording.get('exclamation_mark'))
	exit(1)

try:
	device_manager = DeviceManager()
	device_manager.sync_effects = True
except DaemonNotFound:
	print(wording.get('daemon_no') + wording.get('exclamation_mark'))
	exit(1)


def run(slug, interval):
	data = requests.get('https://api.travis-ci.org/repos/' + slug).json()
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
				print(color.get('yellow') + wording.get('hourglass') + color.get('end') + ' ' + wording.get('build_process').format(item['slug']))
				if status != 'failed':
					status = 'process'
			if item['last_build_status'] == 0:
				print(color.get('green') + wording.get('tick') + color.get('end') + ' ' + wording.get('build_passed').format(item['slug']))
			if item['last_build_status'] == 1:
				print(color.get('red') + wording.get('cross') + color.get('end') + ' ' + wording.get('build_failed').format(item['slug']))
				status = 'failed'

	# handle device

	if len(device_manager.devices) == 0:
		print(wording.get('device_no') + wording.get('exclamation_mark'))
		exit(1)

	# process device

	for device in device_manager.devices:
		if status == 'process' and static(device, [255, 255, 0]):
			print(wording.get('setting_process').format(device.name) + wording.get('point'))
		if status == 'passed' and static(device, [0, 255, 0]):
			print(wording.get('setting_passed').format(device.name) + wording.get('point'))
		if status == 'failed' and pulsate(device, [255, 0, 0]):
			print(wording.get('setting_failed').format(device.name) + wording.get('point'))

	# handle thread

	if interval > 0:
		threading.Timer(interval, run, args=[slug, interval]).start()


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
