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
		from phue import Bridge, PhueRegistrationException, PhueRequestTimeout

		try:
			api = Bridge(ip)
		except (PhueRequestTimeout, OSError, ValueError):
			logger.error(wording.get('connection_not_found').format('PHILIPS HUE') + wording.get('exclamation_mark'))
			sys.exit()
		except PhueRegistrationException:
			logger.error(wording.get('press_button').format('PAIRING', 'PHILIPS HUE BRIDGE') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('PHILIPS HUE') + wording.get('exclamation_mark'))
		sys.exit()
