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
	try:
		from StreamDeck.DeviceManager import DeviceManager, ProbeError

		try:
			return DeviceManager()
		except ProbeError:
			sys.exit(wording.get('connection_not_found').format('ELGATO STREAMDECK') + wording.get('exclamation_mark'))
	except ImportError:
		sys.exit(wording.get('package_not_found').format('STREAMDECK') + wording.get('exclamation_mark'))
