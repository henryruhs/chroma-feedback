from chroma_feedback import wording


def api_factory():
	try:
		from lifxlan import LifxLAN

		return LifxLAN()
	except ImportError:
		exit(wording.get('package_no').format('LIFXLAN') + wording.get('exclamation_mark'))
