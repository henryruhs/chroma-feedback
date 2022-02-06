import asyncio
import sys
from typing import Any

from chroma_feedback import logger, wording

API = None
LOOP = None


def get_api(light_ip : str) -> Any:
	global API

	if not API:
		API = api_factory(light_ip)
	return API


def api_factory(light_ip : str) -> Any:
	try:
		from pywizlight import wizlight
		from pywizlight.exceptions import WizLightConnectionError, WizLightTimeOutError

		try:
			api = wizlight(light_ip, True)
		except (WizLightConnectionError, WizLightTimeOutError):
			logger.error(wording.get('connection_not_found').format('wiz_light') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('pywizlight') + wording.get('exclamation_mark'))
		sys.exit()


def get_loop() -> Any:
	global LOOP

	if not LOOP:
		LOOP = asyncio.get_event_loop()
	return LOOP


def get_builder() -> Any:
	try:
		from pywizlight import PilotBuilder

		return PilotBuilder
	except ImportError:
		logger.error(wording.get('package_not_found').format('WIZ LIGHT') + wording.get('exclamation_mark'))
		sys.exit()
