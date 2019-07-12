from chroma_feedback import wording


def bridge_factory(ip):
	bridge = None

	# handle import

	try:
		from phue import Bridge, PhueRegistrationException, PhueRequestTimeout
	except ImportError:
		exit(wording.get('package_no').format('PHUE') + wording.get('exclamation_mark'))

	# create instance

	try:
		bridge = Bridge(ip)
	except (PhueRequestTimeout, OSError, ValueError):
		exit(wording.get('connection_no').format('PHILIPS HUE') + wording.get('exclamation_mark'))
	except PhueRegistrationException:
		exit(wording.get('press_button').format('PAIRING', 'PHILIPS HUE BRIDGE') + wording.get('exclamation_mark'))
	return bridge
