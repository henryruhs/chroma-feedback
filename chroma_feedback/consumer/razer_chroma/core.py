from chroma_feedback import color, wording
from .factory import api_factory

args = None


def init(program):
	global args

	if not args:
		program.add_argument('--razer-chroma-device', action = 'append')
	args = program.parse_known_args()[0]


def run(status):
	api = api_factory()
	devices = get_devices(api.devices, args.razer_chroma_device)

	if not devices:
		exit(wording.get('device_no') + wording.get('exclamation_mark'))
	return process(status, devices)


def get_devices(devices, device_names):
	if device_names:
		for device in list(devices):
			if device.name not in device_names:
				devices.remove(device)
	return devices


def process(status, devices):
	result = []

	# process devices

	for device in devices:
		if status == 'passed':
			result.append(
			{
				'consumer': 'razer_chroma',
				'name': device.name,
				'active': static(device, color.get_passed_rgb()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'razer_chroma',
				'name': device.name,
				'active': static(device, color.get_process_rgb()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'razer_chroma',
				'name': device.name,
				'active': pulsate(device, color.get_errored_rgb()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'razer_chroma',
				'name': device.name,
				'active': pulsate(device, color.get_failed_rgb()),
				'status': status
			})
	return result


def static(device, state):
	if device.fx.has('logo') and device.fx.has('scroll'):
		return device.fx.misc.logo.static(state['red'], state['green'], state['blue']) and device.fx.misc.scroll_wheel.static(state['red'], state['green'], state['blue'])
	return device.fx.static(state['red'], state['green'], state['blue'])


def pulsate(device, state):
	if device.fx.has('logo') and device.fx.has('scroll'):
		return device.fx.misc.logo.pulsate(state['red'], state['green'], state['blue']) and device.fx.misc.scroll_wheel.pulsate(state['red'], state['green'], state['blue'])
	return device.fx.breath_single(state['red'], state['green'], state['blue'])
