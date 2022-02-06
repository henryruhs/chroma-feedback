import sys
from typing import Any

from chroma_feedback import logger, wording

API = None


def get_api() -> Any:
	global API

	if not API:
		API = api_factory()
	return API


def api_factory() -> Any:
	try:
		from busylight.lights import USBLightIOError, USBLightNotFound
		from busylight.lights.thingm import Blink1 as api

		try:
			api.first_light().release()
		except (USBLightIOError, USBLightNotFound):
			logger.error(wording.get('connection_not_found').format('thingm_blink1') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('busylight-for-humans') + wording.get('exclamation_mark'))
		sys.exit()
