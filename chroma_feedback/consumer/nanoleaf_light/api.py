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
			exit(wording.get('connection_no').format('NANOLEAF LIGHT') + wording.get('exclamation_mark'))
		except NanoleafRegistrationError:
			exit(wording.get('press_button').format('PAIRING', 'NANOLEAF LIGHT') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		exit(wording.get('package_no').format('NANOLEAF LIGHT') + wording.get('exclamation_mark'))
