import asyncio
import sys
from typing import Any
from chroma_feedback import wording

API = None
LOOP = None


def get_api(ip : str) -> Any:
	global API

	if not API:
		API = api_factory(ip)
	return API


def api_factory(ip : str) -> Any:
	api = None

	try:
		from pywizlight import wizlight
		from pywizlight.exceptions import WizLightConnectionError, WizLightTimeOutError

		try:
			api = wizlight(ip, True)
		except (WizLightConnectionError, WizLightTimeOutError):
			sys.exit(wording.get('connection_not_found').format('WIZ LIGHT') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		sys.exit(wording.get('package_not_found').format('WIZ LIGHT') + wording.get('exclamation_mark'))


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
		return None
