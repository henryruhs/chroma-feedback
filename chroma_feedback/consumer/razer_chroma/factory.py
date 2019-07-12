from chroma_feedback import wording


def device_manager_factory():
	device_manager = None

	# handle import

	try:
		from openrazer.client import DeviceManager, DaemonNotFound
	except ImportError:
		exit(wording.get('package_no').format('OPENRAZER') + wording.get('exclamation_mark'))

	# create instance

	try:
		device_manager = DeviceManager()
		device_manager.sync_effects = True
	except DaemonNotFound:
		exit(wording.get('daemon_no').format('RAZER CHROMA') + wording.get('exclamation_mark'))
	return device_manager
