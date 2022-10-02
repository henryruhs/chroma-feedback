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
		from yeelight import Bulb, BulbException

		try:
			api = Bulb(light_ip)
		except BulbException:
			logger.error(wording.get('connection_not_found').format('xiaomi.yeelight') + wording.get('exclamation_mark'))
			sys.exit()
		try:
			api.turn_on()
		except BulbException:
			logger.error(wording.get('enable_feature').format('lan control', 'xiaomi.yeelight') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('yeelight') + wording.get('exclamation_mark'))
		sys.exit()
