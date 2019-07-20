from chroma_feedback import wording
from .factory import api_factory

args = None


def init(program):
	global args

	if not args:
		program.add_argument('--razer-chroma-device', action = 'append')
	args = program.parse_known_args()[0]


def run(status):
	api = api_factory()
	devices = api.devices

	if args.razer_chroma_device:
		for device in list(devices):
			if device.name not in args.razer_chroma_device:
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
				'consumer': 'razer_chroma',
				'name': device.name,
				'active': static(device, [0, 255, 0]),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'razer_chroma',
				'name': device.name,
				'active': static(device, [255, 255, 0]),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'razer_chroma',
				'name': device.name,
				'active': pulsate(device, [255, 255, 255]),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'razer_chroma',
				'name': device.name,
				'active': pulsate(device, [255, 0, 0]),
				'status': status
			})
	return result


def static(device, rgb):
	if device.fx.has('logo') and device.fx.has('scroll'):
		return device.fx.misc.logo.static(rgb[0], rgb[1], rgb[2]) and device.fx.misc.scroll_wheel.static(rgb[0], rgb[1], rgb[2])
	return device.fx.static(rgb[0], rgb[1], rgb[2])


def pulsate(device, rgb):
	if device.fx.has('logo') and device.fx.has('scroll'):
		return device.fx.misc.logo.pulsate(rgb[0], rgb[1], rgb[2]) and device.fx.misc.scroll_wheel.pulsate(rgb[0], rgb[1], rgb[2])
	return device.fx.breath_single(rgb[0], rgb[1], rgb[2])
