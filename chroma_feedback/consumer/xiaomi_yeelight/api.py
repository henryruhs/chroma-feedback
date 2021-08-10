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
		from yeelight import Bulb, BulbException

		try:
			api = Bulb(ip)
		except BulbException:
			sys.exit(wording.get('connection_not_found').format('XIAOMI YEELIGHT') + wording.get('exclamation_mark'))
		try:
			api.turn_on()
		except BulbException:
			sys.exit(wording.get('enable_feature').format('LAN CONTROL', 'XIAOMI YEELIGHT') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		sys.exit(wording.get('package_not_found').format('XIAOMI YEELIGHT') + wording.get('exclamation_mark'))
