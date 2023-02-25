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
		from liquidctl.driver.rgb_fusion2 import RgbFusion2 as api

		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('liquidctl') + wording.get('exclamation_mark'))
		sys.exit()
