import sys
from typing import Any
from chroma_feedback import logger, wording

API = None


def get_api(ip : str) -> Any:
	global API

	if not API:
		API = api_factory(ip)
	return API


def api_factory(ip : str) -> Any:
	try:
		from nanoleafapi import Nanoleaf, NanoleafConnectionError, NanoleafRegistrationError

		try:
			api = Nanoleaf(ip)
		except NanoleafConnectionError:
			logger.error(wording.get('connection_not_found').format('NANOLEAF LIGHT') + wording.get('exclamation_mark'))
			sys.exit()
		except NanoleafRegistrationError:
			logger.error(wording.get('press_button').format('PAIRING', 'NANOLEAF LIGHT') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('NANOLEAF LIGHT') + wording.get('exclamation_mark'))
		sys.exit()
