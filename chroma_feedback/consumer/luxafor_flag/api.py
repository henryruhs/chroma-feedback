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
			api.all_lights()
		except (USBLightIOError, USBLightNotFound):
			exit(wording.get('connection_no').format('LUXAFOR FLAG') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		exit(wording.get('package_no').format('BUSYLIGHT FOR HUMANS') + wording.get('exclamation_mark'))
