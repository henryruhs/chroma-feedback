from chroma_feedback import wording


def api_factory():
	api = None

	try:
		from blink1.blink1 import Blink1, Blink1ConnectionFailed

		try:
			api = Blink1()
		except Blink1ConnectionFailed:
			exit(wording.get('connection_no').format('THINGM BLINK') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		exit(wording.get('package_no').format('BLINK1') + wording.get('exclamation_mark'))
