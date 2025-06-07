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
		from liquidctl.driver.rgb_fusion2 import RgbFusion2 as api

		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('liquidctl') + wording.get('exclamation_mark'))
		sys.exit()
