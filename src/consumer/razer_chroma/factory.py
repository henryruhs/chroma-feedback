from src import wording

try:
	from openrazer.client import DeviceManager, DaemonNotFound
except ImportError:
	exit(wording.get('driver_no') + wording.get('exclamation_mark'))


def device_manager_factory():
	device_manager = None
	try:
		device_manager = DeviceManager()
		device_manager.sync_effects = True
	except DaemonNotFound:
		exit(wording.get('daemon_no') + wording.get('exclamation_mark'))
	return device_manager
