from __future__ import print_function
import os
import threading
import src.miner as miner
import src.reporter as reporter
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
	data = miner.mine_data(args)

	# handle data

	if len(data) == 0:
		exit(wording.get('data_no') + wording.get('exclamation_mark'))

	# process data

	result = reporter.process_data(data)
	if result:
		reporter.print_result(result)
		print()

	# handle device

	if len(device_manager.devices) == 0:
		exit(wording.get('device_no') + wording.get('exclamation_mark'))

	# process device

	if args.dry_run is False:
		result = process_device(result['status'])
		if result:
			reporter.print_result(result)
			print()

	# handle thread

	if args.background_run is True:
		threading.Timer(args.background_interval, run, args =
		[
			args
		]).start()


def process_device(status):
	message = []

	# process device

	for device in device_manager.devices:
		if status == 'passed' and static(device.fx, [0, 255, 0]):
			message.append(wording.get('setting_passed').format(device.name) + wording.get('point'))
		if status == 'process' and static(device.fx, [255, 255, 0]):
			message.append(wording.get('setting_process').format(device.name) + wording.get('point'))
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
