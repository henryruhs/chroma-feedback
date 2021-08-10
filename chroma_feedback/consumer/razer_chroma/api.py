import sys
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
			sys.exit(wording.get('daemon_not_found').format('RAZER CHROMA') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		sys.exit(wording.get('package_not_found').format('OPENRAZER META') + wording.get('exclamation_mark'))
