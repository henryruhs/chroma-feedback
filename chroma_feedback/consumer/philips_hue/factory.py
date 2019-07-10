from chroma_feedback import wording


def bridge_factory(ip):
	bridge = None

	# handle import

	try:
		from phue import Bridge, PhueRegistrationException
	except ImportError:
		exit(wording.get('package_no').format('PHUE') + wording.get('exclamation_mark'))

	# create instance

	try:
		bridge = Bridge(ip)
	except PhueRegistrationException:
		exit(wording.get('connection_no').format('BRIDGE') + wording.get('exclamation_mark') + ' ' + wording.get('press_button').format('PAIRING') + wording.get('exclamation_mark'))
	return bridge
