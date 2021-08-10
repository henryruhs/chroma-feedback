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
		from busylight.lights import USBLightIOError, USBLightNotFound
		from busylight.lights.luxafor import Flag

		try:
			api = Flag
			api.first_light().release()
		except (USBLightIOError, USBLightNotFound):
			sys.exit(wording.get('connection_not_found').format('LUXAFOR FLAG') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		sys.exit(wording.get('package_not_found').format('BUSYLIGHT FOR HUMANS') + wording.get('exclamation_mark'))
