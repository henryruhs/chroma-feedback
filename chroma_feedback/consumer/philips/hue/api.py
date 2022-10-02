import sys
from typing import Any

from chroma_feedback import logger, wording

API = None


def get_api(bridge_ip : str) -> Any:
	global API

	if not API:
		API = api_factory(bridge_ip)
	return API


def api_factory(bridge_ip : str) -> Any:
	try:
		from phue import Bridge, PhueRegistrationException, PhueRequestTimeout

		try:
			api = Bridge(bridge_ip)
		except (PhueRequestTimeout, OSError, ValueError):
			logger.error(wording.get('connection_not_found').format('philips.hue') + wording.get('exclamation_mark'))
			sys.exit()
		except PhueRegistrationException:
			logger.error(wording.get('press_button').format('pairing', 'philips.hue') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('phue') + wording.get('exclamation_mark'))
		sys.exit()
