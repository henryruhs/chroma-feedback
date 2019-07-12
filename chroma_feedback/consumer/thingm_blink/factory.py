from chroma_feedback import wording


def blink_factory():
	blink = None

	# handle import

	try:
		from blink1.blink1 import Blink1, Blink1ConnectionFailed
	except ImportError:
		exit(wording.get('package_no').format('BLINK1') + wording.get('exclamation_mark'))

	# create instance

	try:
		blink = Blink1()
	except Blink1ConnectionFailed:
		exit(wording.get('connection_no').format('THINGM BLINK') + wording.get('exclamation_mark'))
	return blink
