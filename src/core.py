from __future__ import print_function
import os
import threading
import src.device as device
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
	data = miner.process_data(args)

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
		result = device.process_device(device_manager.devices, result['status'])
		if result:
			reporter.print_result(result)
			print()

	# handle thread

	if args.background_run is True:
		threading.Timer(args.background_interval, run, args =
		[
			args
		]).start()


def destroy(number, frame):
	print('\r' + wording.get('goodbye') + wording.get('exclamation_mark'))
	os._exit(0)
