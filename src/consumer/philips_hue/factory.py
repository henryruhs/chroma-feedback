from src import wording


def bridge_factory(host):
	bridge = None

	# handle import

	try:
		from phue import Bridge, PhueRegistrationException
	except ImportError:
		exit(wording.get('package_no').format('PHUE') + wording.get('exclamation_mark'))

	# create instance

	try:
		bridge = Bridge(host)
	except PhueRegistrationException as exception:
		exit(exception)
	return bridge
