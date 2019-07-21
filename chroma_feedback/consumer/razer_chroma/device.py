import copy
from chroma_feedback import color


def get_devices(devices, device_names):
	if device_names:
		for device in copy.copy(devices):
			if device.name not in device_names:
				devices.remove(device)
	return devices


def process_devices(status, devices):
	result = []

	# process devices

	for device in devices:
		if status == 'passed':
			result.append(
			{
				'consumer': 'razer_chroma',
				'type': 'device',
				'name': device.name,
				'active': static_device(device, color.get_passed_rgb()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'razer_chroma',
				'type': 'device',
				'name': device.name,
				'active': static_device(device, color.get_process_rgb()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'razer_chroma',
				'type': 'device',
				'name': device.name,
				'active': pulsate_device(device, color.get_errored_rgb()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'razer_chroma',
				'type': 'device',
				'name': device.name,
				'active': pulsate_device(device, color.get_failed_rgb()),
				'status': status
			})
	return result


def static_device(device, state):
	if device.fx.has('logo') and device.fx.has('scroll'):
		return device.fx.misc.logo.static(state['red'], state['green'], state['blue']) and device.fx.misc.scroll_wheel.static(state['red'], state['green'], state['blue'])
	return device.fx.static(state['red'], state['green'], state['blue'])


def pulsate_device(device, state):
	if device.fx.has('logo') and device.fx.has('scroll'):
		return device.fx.misc.logo.pulsate(state['red'], state['green'], state['blue']) and device.fx.misc.scroll_wheel.pulsate(state['red'], state['green'], state['blue'])
	return device.fx.breath_single(state['red'], state['green'], state['blue'])
