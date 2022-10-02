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
		from lifxlan import LifxLAN, WorkflowException

		try:
			api = LifxLAN()
		except WorkflowException:
			logger.error(wording.get('connection_not_found').format('lifx') + wording.get('exclamation_mark'))
			sys.exit()
		return api
	except ImportError:
		logger.error(wording.get('package_not_found').format('lifxlan') + wording.get('exclamation_mark'))
		sys.exit()
