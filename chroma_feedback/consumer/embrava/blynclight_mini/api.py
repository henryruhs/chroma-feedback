import sys

from chroma_feedback import logger, wording
from chroma_feedback.types import Api

API : Api = None


def get_api() -> Api:
	global API

	if not API:
		API = api_factory()
	return API


def api_factory() -> Api:
	try:
		from busylight.lights import NoLightsFound, LightUnavailable
		from busylight.lights.embrava import Blynclight_Mini as api

		try:
			api.first_light().release()
		except (NoLightsFound, LightUnavailable):
			logger.error(wording.get('connection_not_found').format('embrava.blynclight_mini') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('busylight-for-humans') + wording.get('exclamation_mark'))
		sys.exit()
