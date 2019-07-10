from chroma_feedback import wording
from .factory import blink_factory

args = None
blink = None

def init(program):
	global args

	if not args:
		program.add_argument('--thingm-blink-device', action = 'append')
	args = program.parse_known_args()[0]


def run(status):
	global blink

	if not blink:
		blink = blink_factory()
	devices = blink.list()

	if args.thingm_blink_device:
		for device in list(devices):
			if device not in args.thingm_blink_device:
				devices.remove(device)
	if not devices:
		exit(wording.get('device_no') + wording.get('exclamation_mark'))
	return process(status, devices)


def process(status, devices):
	result = []

	# process devices

	for device in devices:
		if status == 'passed':
			result.append(
			{
				'consumer': 'thingm_blink',
				'name': device,
				'active': static([0, 255, 0]),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'thingm_blink',
				'name': device,
				'active': static([255, 255, 0]),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'thingm_blink',
				'name': device,
				'active': pulsate([255, 255, 255]),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'thingm_blink',
				'name': device,
				'active': pulsate([255, 0, 0]),
				'status': status
			})
	return result


def static(rgb):
	return blink is not None and blink.fade_to_rgb(100, rgb[0], rgb[1], rgb[2]) is None


def pulsate(rgb):
	return blink is not None and blink.fade_to_rgb(100, rgb[0], rgb[1], rgb[2]) is None
