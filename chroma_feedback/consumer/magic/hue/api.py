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
		from magichue import LocalLight

		try:
			api = LocalLight(light_ip)
		except OSError:
			logger.error(wording.get('connection_not_found').format('magic.hue') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('python-magichue') + wording.get('exclamation_mark'))
		sys.exit()


def get_modes() -> Any:
	try:
		from magichue import modes

		return modes
	except ImportError:
		logger.error(wording.get('package_not_found').format('magic_hue') + wording.get('exclamation_mark'))
		sys.exit()
