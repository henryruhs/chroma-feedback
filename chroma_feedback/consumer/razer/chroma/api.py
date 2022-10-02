import sys
from typing import Any

from chroma_feedback import logger, wording

API = None


def get_api() -> Any:
	global API

	if not API:
		API = api_factory()
	return API


def api_factory() -> Any:
	try:
		from openrazer.client import DeviceManager, DaemonNotFound

		try:
			api = DeviceManager()
		except DaemonNotFound:
			logger.error(wording.get('daemon_not_found').format('razer.chroma') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('openrazer') + wording.get('exclamation_mark'))
		sys.exit()
