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
			exit(wording.get('connection_no').format('PHILIPS HUE') + wording.get('exclamation_mark'))
		except PhueRegistrationException:
			exit(wording.get('press_button').format('PAIRING', 'PHILIPS HUE BRIDGE') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		exit(wording.get('package_no').format('PHILIPS HUE') + wording.get('exclamation_mark'))
