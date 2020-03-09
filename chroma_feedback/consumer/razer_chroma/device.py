from typing import Any, Dict, List
import copy
from chroma_feedback import color


def get_devices(devices : Any, device_names : List[str]) -> Any:
	if device_names:
		for device in copy.copy(devices):
			if device.name not in device_names:
				devices.remove(device)
	return devices


def process_devices(devices : Any, status : str) -> List[Dict[str, Any]]:
	result = []

	# process devices

	for device in devices:
		if status == 'passed':
			result.append(
			{
				'consumer': 'razer_chroma',
				'type': 'device',
				'name': device.name,
				'active': static_device(device, color.get_passed()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'razer_chroma',
				'type': 'device',
				'name': device.name,
				'active': static_device(device, color.get_process()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'razer_chroma',
				'type': 'device',
				'name': device.name,
				'active': pulsate_device(device, color.get_errored()) or breath_device(device, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'razer_chroma',
				'type': 'device',
				'name': device.name,
				'active': pulsate_device(device, color.get_failed()) or breath_device(device, color.get_failed()),
				'status': status
			})
	return result


def static_device(device : Any, state : Dict[str, Any]) -> bool:
	if device.has('brightness'):
		device.brightness = state['brightness'][0]
	if device.fx.has('static'):
		return device.fx.static(state['rgb'][0], state['rgb'][1], state['rgb'][2])
	return misc_effect(device, state, 'static')


def pulsate_device(device : Any, state : Dict[str, Any]) -> bool:
	if device.has('brightness'):
		device.brightness = state['brightness'][0]
	if device.fx.has('pulsate'):
		return device.fx.breath_single(state['rgb'][0], state['rgb'][1], state['rgb'][2])
	return misc_effect(device, state, 'pulsate')


def breath_device(device : Any, state : Dict[str, Any]) -> bool:
	if device.has('brightness'):
		device.brightness = state['brightness'][0]
	if device.fx.has('breath_single'):
		return device.fx.breath_single(state['rgb'][0], state['rgb'][1], state['rgb'][2])
	return misc_effect(device, state, 'breath_single')


def misc_effect(device : Any, state : Dict[str, Any], effect_name : str) -> bool:
	effect_state = False
	parts =\
	{
		'logo': 'logo',
		'scroll': 'scroll_wheel',
		'left': 'left',
		'right': 'right',
		'backlight': 'backlight'
	}

	for part_key, part_value in parts.items():
		if device.fx.has(part_key + '_' + effect_name):
			effect_function = getattr(getattr(device.fx.misc, part_value), effect_name)
			effect_state = effect_function(state['rgb'][0], state['rgb'][1], state['rgb'][2]) or effect_state
	return effect_state
