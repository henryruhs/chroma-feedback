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
		from nanoleafapi import Nanoleaf, NanoleafConnectionError, NanoleafRegistrationError

		try:
			api = Nanoleaf(ip)
		except NanoleafConnectionError:
			sys.exit(wording.get('connection_not_found').format('NANOLEAF LIGHT') + wording.get('exclamation_mark'))
		except NanoleafRegistrationError:
			sys.exit(wording.get('press_button').format('PAIRING', 'NANOLEAF LIGHT') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		sys.exit(wording.get('package_not_found').format('NANOLEAF LIGHT') + wording.get('exclamation_mark'))
