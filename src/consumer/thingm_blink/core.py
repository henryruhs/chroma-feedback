from src import wording
from .factory import blink_factory

args = None
blink = None

def init(program):
	global args

	args = program.parse_known_args()[0]


def run(status):
	global blink

	blink = blink_factory()
	devices = blink.list()

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
	return blink is not None and blink.fade_to_rgb(1000, rgb[0], rgb[1], rgb[2])


def pulsate(rgb):
	return blink is not None and blink.fade_to_rgb(1000, rgb[0], rgb[1], rgb[2])
