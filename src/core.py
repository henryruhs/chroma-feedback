from __future__ import print_function
from xml.etree import ElementTree
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
	response = requests.get('https://api.travis-ci.org/repos/' + slug, headers =
	{
		'accept': 'application/xml'
	})
	try:
		data = ElementTree.XML(response.content)
		status = 'passed'
	except ElementTree.ParseError:
		exit(1)

	# process data

	for item in data:
		if item.attrib['lastBuildStatus'] == 'Unknown':
			print(color.get('yellow') + wording.get('hourglass') + color.get('end') + ' ' + wording.get('build_process').format(item.attrib['name']))
			if status != 'failed' and status != 'errored':
				status = 'process'
		if item.attrib['lastBuildStatus'] == 'Error':
			print(color.get('white') + wording.get('cross') + color.get('end') + ' ' + wording.get('build_errored').format(item.attrib['name']))
			if status != 'failed':
				status = 'errored'
		if item.attrib['lastBuildStatus'] == 'Success':
			print(color.get('green') + wording.get('tick') + color.get('end') + ' ' + wording.get('build_passed').format(item.attrib['name']))
		if item.attrib['lastBuildStatus'] == 'Failure':
			print(color.get('red') + wording.get('cross') + color.get('end') + ' ' + wording.get('build_failed').format(item.attrib['name']))
			status = 'failed'

	# handle device

	if len(device_manager.devices) == 0:
		print(wording.get('device_no') + wording.get('exclamation_mark'))
		exit(1)

	# process device

	for device in device_manager.devices:
		if status == 'process' and static(device, [255, 255, 0]):
			print(wording.get('setting_process').format(device.name) + wording.get('point'))
		if status == 'errored' and pulsate(device, [255, 255, 255]):
			print(wording.get('setting_errored').format(device.name) + wording.get('point'))
		if status == 'passed' and static(device, [0, 255, 0]):
			print(wording.get('setting_passed').format(device.name) + wording.get('point'))
		if status == 'failed' and pulsate(device, [255, 0, 0]):
			print(wording.get('setting_failed').format(device.name) + wording.get('point'))

	# handle thread

	if interval > 0:
		threading.Timer(interval, run, args =
		[
			slug,
			interval
		]).start()


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
