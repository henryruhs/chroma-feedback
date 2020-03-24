from typing import Any
from chroma_feedback import wording

API = None


def get_api() -> Any:
	global API

	if not API:
		API = api_factory()
	return API


def api_factory() -> Any:
	api = None

	try:
		from lifxlan import LifxLAN, WorkflowException

		try:
			api = LifxLAN()
		except WorkflowException:
			exit(wording.get('connection_no').format('LIFX LIGHT') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		exit(wording.get('package_no').format('LIFX LIGHT') + wording.get('exclamation_mark'))
