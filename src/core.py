from __future__ import print_function
import os
import threading
import src.color as color
import src.provider.appveyor as appveyor
import src.provider.circle as circle
import src.provider.travis as travis
import src.wording as wording

try:
	from openrazer.client import DeviceManager, DaemonNotFound
except ImportError:
	exit(wording.get('driver_no') + wording.get('exclamation_mark'))

try:
	device_manager = DeviceManager()
	device_manager.sync_effects = True
except DaemonNotFound:
	exit(wording.get('daemon_no') + wording.get('exclamation_mark'))


def run(args):
	data = mine_data(args)

	# handle data

	if len(data) == 0:
		exit(wording.get('data_no') + wording.get('exclamation_mark'))

	# process status

	status = process_status(data)

	# handle device

	if len(device_manager.devices) == 0:
		exit(wording.get('device_no') + wording.get('exclamation_mark'))

	# process device

	if args.dry_run is False:
		process_device(status)

	# handle thread

	if args.background_run is True:
		threading.Timer(args.background_interval, run, args =
		[
			args
		]).start()


def mine_data(args):
	data = []
	for provider in args.provider:
		for slug in args.slug:
			data.extend(fetch_data(provider, slug))
	return data


def fetch_data(provider, slug):
	if provider == 'appveyor':
		return appveyor.fetch_data(slug)
	if provider == 'circle':
		return circle.fetch_data(slug)
	if provider == 'travis':
		return travis.fetch_data(slug)
	return []


def process_status(data):
	status = 'passed'

	# process data

	for item in data:
		if item['active'] is True:
			if item['status'] == 'process':
				print(color.yellow(wording.get('hourglass')) + ' ' + wording.get('build_process').format(item['slug'], item['provider']))
				if status != 'errored' and status != 'failed':
					status = 'process'
			if item['status'] == 'passed':
				print(color.green(wording.get('tick')) + ' ' + wording.get('build_passed').format(item['slug'], item['provider']))
			if item['status'] == 'errored':
				print(wording.get('cross') + ' ' + wording.get('build_errored').format(item['slug'], item['provider']))
				if status != 'failed':
					status = 'errored'
			if item['status'] == 'failed':
				print(color.red(wording.get('cross')) + ' ' + wording.get('build_failed').format(item['slug'], item['provider']))
				status = 'failed'
	return status


def process_device(status):
	for device in device_manager.devices:
		if status == 'process' and static(device.fx, [255, 255, 0]):
			print(wording.get('setting_process').format(device.name) + wording.get('point'))
		if status == 'passed' and static(device.fx, [0, 255, 0]):
			print(wording.get('setting_passed').format(device.name) + wording.get('point'))
		if status == 'errored' and pulsate(device.fx, [255, 255, 255]):
			print(wording.get('setting_errored').format(device.name) + wording.get('point'))
		if status == 'failed' and pulsate(device.fx, [255, 0, 0]):
			print(wording.get('setting_failed').format(device.name) + wording.get('point'))


def static(fx, rgb):
	if fx.has('logo') and fx.has('scroll'):
		return fx.misc.logo.static(rgb[0], rgb[1], rgb[2]) and fx.misc.scroll_wheel.static(rgb[0], rgb[1], rgb[2])
	return fx.static(rgb[0], rgb[1], rgb[2])


def pulsate(fx, rgb):
	if fx.has('logo') and fx.has('scroll'):
		return fx.misc.logo.pulsate(rgb[0], rgb[1], rgb[2]) and fx.misc.scroll_wheel.pulsate(rgb[0], rgb[1], rgb[2])
	return fx.breath_single(rgb[0], rgb[1], rgb[2])


def destroy(number, frame):
	print('\r' + wording.get('goodbye') + wording.get('exclamation_mark'))
	os._exit(0)
