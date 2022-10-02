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
		from StreamDeck.DeviceManager import DeviceManager, ProbeError

		try:
			api = DeviceManager()
			api.enumerate()
		except ProbeError:
			logger.error(wording.get('connection_not_found').format('elgato.streamdeck') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('streamdeck') + wording.get('exclamation_mark'))
		sys.exit()
