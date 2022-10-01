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
		from busylight.lights import LightUnavailable, LightNotFound
		from busylight.lights.compulap import Fit_StatUSB as api

		try:
			api.first_light().is_pluggedin()
		except (LightUnavailable, LightNotFound):
			logger.error(wording.get('connection_not_found').format('compulab_fit_statusb') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('busylight-for-humans') + wording.get('exclamation_mark'))
		sys.exit()
