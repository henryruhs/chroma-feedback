from typing import Any
from chroma_feedback import wording

API = None


def get_api() -> Any:
	global API

	if not API:
		API = api_factory()
	return API


def api_factory() -> Any:
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
		exit(wording.get('package_no').format('OPENRAZER META') + wording.get('exclamation_mark'))
