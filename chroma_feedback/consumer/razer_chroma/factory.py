from chroma_feedback import wording


def api_factory():
	api = None

	try:
		from openrazer.client import DeviceManager, DaemonNotFound

		try:
			api = DeviceManager()
			api.sync_effects = True
		except DaemonNotFound:
			exit(wording.get('daemon_no').format('RAZER CHROMA') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		exit(wording.get('package_no').format('OPENRAZER') + wording.get('exclamation_mark'))
