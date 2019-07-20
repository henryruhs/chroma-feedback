from chroma_feedback import wording

api = None


def get_api():
	global api

	if not api:
		api = factory()
	return api


def factory():
	try:
		from lifxlan import LifxLAN

		return LifxLAN()
	except ImportError:
		exit(wording.get('package_no').format('LIFXLAN') + wording.get('exclamation_mark'))
