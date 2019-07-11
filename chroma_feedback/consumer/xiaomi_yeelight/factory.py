from chroma_feedback import wording


def bulb_factory(ip):
	bulb = None

	# handle import

	try:
		from yeelight import Bulb, BulbException
	except ImportError:
		exit(wording.get('package_no').format('YEELIGHT') + wording.get('exclamation_mark'))

	# create instance

	try:
		bulb = Bulb(ip)
		bulb.turn_on()
	except BulbException:
		exit(wording.get('connection_no').format('YEELIGHT') + wording.get('exclamation_mark'))
	return bulb
