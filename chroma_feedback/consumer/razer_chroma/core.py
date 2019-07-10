from chroma_feedback import wording
from .factory import device_manager_factory

args = None


def init(program):
	global args

	if not args:
		program.add_argument('--razer-chroma-device', action = 'append')
	args = program.parse_known_args()[0]


def run(status):
	device_manager = device_manager_factory()
	devices = device_manager.devices

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
				'active': static(device.fx, [0, 255, 0]),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'razer_chroma',
				'name': device.name,
				'active': static(device.fx, [255, 255, 0]),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'razer_chroma',
				'name': device.name,
				'active': pulsate(device.fx, [255, 255, 255]),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'razer_chroma',
				'name': device.name,
				'active': pulsate(device.fx, [255, 0, 0]),
				'status': status
			})
	return result


def static(fx, rgb):
	if fx.has('logo') and fx.has('scroll'):
		return fx.misc.logo.static(rgb[0], rgb[1], rgb[2]) and fx.misc.scroll_wheel.static(rgb[0], rgb[1], rgb[2])
	return fx.static(rgb[0], rgb[1], rgb[2])


def pulsate(fx, rgb):
	if fx.has('logo') and fx.has('scroll'):
		return fx.misc.logo.pulsate(rgb[0], rgb[1], rgb[2]) and fx.misc.scroll_wheel.pulsate(rgb[0], rgb[1], rgb[2])
	return fx.breath_single(rgb[0], rgb[1], rgb[2])
