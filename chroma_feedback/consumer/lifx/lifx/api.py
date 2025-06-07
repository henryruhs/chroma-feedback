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
