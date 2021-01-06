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
		from pywizlight import wizlight

		try:
			api = wizlight(ip)
		except OSError:
			exit(wording.get('connection_no').format('WIZ LIGHT') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		exit(wording.get('package_no').format('WIZ LIGHT') + wording.get('exclamation_mark'))


def get_builder() -> Any:
	try:
		from pywizlight import PilotBuilder

		return PilotBuilder
	except ImportError:
		return None
