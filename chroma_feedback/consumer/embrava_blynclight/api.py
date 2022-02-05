import sys
from typing import Any
from chroma_feedback import logger, wording

API = None
LIGHTS = None


def get_api() -> Any:
	global API

	if not API:
		API = api_factory()
	return API


def api_factory() -> Any:
	try:
		from busylight.lights import USBLightIOError, USBLightNotFound
		from busylight.lights.embrava import Blynclight as api

		try:
			api.first_light().release()
		except (USBLightIOError, USBLightNotFound):
			logger.error(wording.get('connection_not_found').format('EMBRAVA BLYNCLIGHT') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('BUSYLIGHT FOR HUMANS') + wording.get('exclamation_mark'))
		sys.exit()


def get_lights() -> Any:
	global LIGHTS

	if not LIGHTS:
		LIGHTS = get_api().all_lights()
	return LIGHTS
