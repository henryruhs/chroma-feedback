import sys
from typing import Any

from chroma_feedback import logger, wording

API = None


def get_api(light_ip : str) -> Any:
	global API

	if not API:
		API = api_factory(light_ip)
	return API


def api_factory(light_ip : str) -> Any:
	try:
		from nanoleafapi import Nanoleaf, NanoleafConnectionError, NanoleafRegistrationError

		try:
			api = Nanoleaf(light_ip)
		except NanoleafConnectionError:
			logger.error(wording.get('connection_not_found').format('nanoleaf') + wording.get('exclamation_mark'))
			sys.exit()
		except NanoleafRegistrationError:
			logger.error(wording.get('press_button').format('pairing', 'nanoleaf') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('nanoleafapi') + wording.get('exclamation_mark'))
		sys.exit()
