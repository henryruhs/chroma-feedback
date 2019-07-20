from chroma_feedback import color, wording
from .factory import api_factory

args = None
api = None

def init(program):
	global args

	if not args:
		program.add_argument('--thingm-blink-device', action = 'append')
	args = program.parse_known_args()[0]


def run(status):
	global api

	if not api:
		api = api_factory()
	devices = api.list()

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
				'active': static(color.get_passed_rgb()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'thingm_blink',
				'name': device,
				'active': static(color.get_process_rgb()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'thingm_blink',
				'name': device,
				'active': static(color.get_errored_rgb()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'thingm_blink',
				'name': device,
				'active': static(color.get_failed_rgb()),
				'status': status
			})
	return result


def static(state):
	return api is not None and api.fade_to_rgb(100, state['red'], state['green'], state['blue']) is None
