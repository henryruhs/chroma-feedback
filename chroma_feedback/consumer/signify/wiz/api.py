import sys

from chroma_feedback import logger, wording
from chroma_feedback.consumer.signify.wiz.types import Builder
from chroma_feedback.types import Api

API : Api = None


def get_api(light_ip : str) -> Api:
	global API

	if not API:
		API = api_factory(light_ip)
	return API


def api_factory(light_ip : str) -> Api:
	try:
		from pywizlight import wizlight
		from pywizlight.exceptions import WizLightConnectionError, WizLightTimeOutError

		try:
			api = wizlight(light_ip)
		except (WizLightConnectionError, WizLightTimeOutError):
			logger.error(wording.get('connection_not_found').format('signify.wiz') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('pywizlight') + wording.get('exclamation_mark'))
		sys.exit()


def get_builder() -> Builder:
	try:
		from pywizlight import PilotBuilder

		return PilotBuilder
	except ImportError:
		logger.error(wording.get('package_not_found').format('pywizlight') + wording.get('exclamation_mark'))
		sys.exit()
