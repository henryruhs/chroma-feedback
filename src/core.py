from __future__ import print_function
import os
import threading
from src import device, miner, reporter, wording

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
	if threading.active_count() == 1:
		reporter.header()
		print()

	# process miner

	data = miner.process(args)

	# handle data

	if len(data) == 0:
		exit(wording.get('data_no') + wording.get('exclamation_mark'))

	# process data

	result = reporter.process(data)
	if result:
		reporter.log(result)
		print()

	# handle dry run

	if args.dry_run is False:

		# handle device

		if len(device_manager.devices) == 0:
			exit(wording.get('device_no') + wording.get('exclamation_mark'))

		# process device

		result = device.process(device_manager.devices, result['status'])
		if result:
			reporter.log(result)
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
