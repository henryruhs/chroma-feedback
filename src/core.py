from __future__ import print_function
import os
import threading
import src.color as color
import src.provider.appveyor as appveyor
import src.provider.circle as circle
import src.provider.jenkins as jenkins
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

	# print status

	result = process_data(data)
	if 'message' in result:
		for message in result['message']:
			print(message)
		print()

	# handle device

	if len(device_manager.devices) == 0:
		exit(wording.get('device_no') + wording.get('exclamation_mark'))

	# print device

	if args.dry_run is False:
		result = process_device(result['status'])
		if 'message' in result:
			for message in result:
				print(message)

	# handle thread

	if args.background_run is True:
		threading.Timer(args.background_interval, run, args =
		[
			args
		]).start()


def mine_data(args):
	data = []
	for provider in args.provider:
		if args.slug:
			for slug in args.slug:
				data.extend(fetch_data(provider, args.host, slug, None))
		if args.token:
			data.extend(fetch_data(provider, args.host, None, args.token))
	return data


def fetch_data(provider, host, slug, token):
	if provider == 'appveyor':
		return appveyor.fetch_data(slug, token)
	if provider == 'circle':
		return circle.fetch_data(slug, token)
	if provider == 'jenkins':
		return jenkins.fetch_data(host, slug)
	if provider == 'travis':
		return travis.fetch_data(slug)
	return []


def process_data(data):
	message = []
	status = 'passed'

	# process data

	for item in data:
		if item['active'] is True:
			if item['status'] == 'process':
				message.append(color.yellow(wording.get('hourglass')) + ' ' + wording.get('build_process').format(item['slug'], item['provider']))
				if status != 'errored' and status != 'failed':
					status = 'process'
			if item['status'] == 'passed':
				message.append(color.green(wording.get('tick')) + ' ' + wording.get('build_passed').format(item['slug'], item['provider']))
			if item['status'] == 'errored':
				message.append(wording.get('cross') + ' ' + wording.get('build_errored').format(item['slug'], item['provider']))
				if status != 'failed':
					status = 'errored'
			if item['status'] == 'failed':
				message.append(color.red(wording.get('cross')) + ' ' + wording.get('build_failed').format(item['slug'], item['provider']))
				status = 'failed'
	return\
	{
		'message': message,
		'status': status
	}


def process_device(status):
	message = []

	# process device

	for device in device_manager.devices:
		if status == 'process' and static(device.fx, [255, 255, 0]):
			message.append(wording.get('setting_process').format(device.name) + wording.get('point'))
		if status == 'passed' and static(device.fx, [0, 255, 0]):
			message.append(wording.get('setting_passed').format(device.name) + wording.get('point'))
		if status == 'errored' and pulsate(device.fx, [255, 255, 255]):
			message.append(wording.get('setting_errored').format(device.name) + wording.get('point'))
		if status == 'failed' and pulsate(device.fx, [255, 0, 0]):
			message.append(wording.get('setting_failed').format(device.name) + wording.get('point'))
	return\
	{
		'message': message,
		'status': status
	}


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
