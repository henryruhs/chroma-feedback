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
		from magichue import Light

		try:
			api = Light(ip)
		except OSError:
			sys.exit(wording.get('connection_not_found').format('MAGIC HUE') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		sys.exit(wording.get('package_not_found').format('MAGIC HUE') + wording.get('exclamation_mark'))


def get_modes() -> Any:
	try:
		from magichue import modes

		return modes
	except ImportError:
		return None
