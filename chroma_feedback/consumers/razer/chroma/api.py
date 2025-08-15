import sys

from chroma_feedback import logger, wording
from chroma_feedback.types import Api

API : Api = None


def get_api() -> Api:
	global API

	if not API:
		API = api_factory()
	return API


def api_factory() -> Api:
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
