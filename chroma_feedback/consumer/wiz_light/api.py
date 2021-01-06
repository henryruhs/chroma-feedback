import asyncio
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
		from pywizlight.exceptions import WizLightError

		try:
			api = wizlight(ip)
			builder = get_builder()
			get_loop().run_until_complete(api.turn_on(builder()))
		except WizLightError:
			exit(wording.get('connection_no').format('WIZ LIGHT') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		exit(wording.get('package_no').format('WIZ LIGHT') + wording.get('exclamation_mark'))


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
