import sys
from typing import Any
from chroma_feedback import wording

API = None


def get_api(ip : str) -> Any:
	global API

	if not API:
		API = api_factory(ip)
	return API


def api_factory(ip : str) -> Any:
	api = None

	try:
		from phue import Bridge, PhueRegistrationException, PhueRequestTimeout

		try:
			api = Bridge(ip)
		except (PhueRequestTimeout, OSError, ValueError):
			sys.exit(wording.get('connection_not_found').format('PHILIPS HUE') + wording.get('exclamation_mark'))
		except PhueRegistrationException:
			sys.exit(wording.get('press_button').format('PAIRING', 'PHILIPS HUE BRIDGE') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		sys.exit(wording.get('package_not_found').format('PHILIPS HUE') + wording.get('exclamation_mark'))
