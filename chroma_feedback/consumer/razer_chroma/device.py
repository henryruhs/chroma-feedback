from typing import Any, List
import copy
from chroma_feedback import color
from chroma_feedback.typing import StatusType, ConsumerModel, ColorConfigModel


def get_devices(devices : Any, device_names : List[str]) -> Any:
	if device_names:
		for device in copy.copy(devices):
			if device.name not in device_names:
				devices.remove(device)
	return devices


def process_devices(devices : Any, status : StatusType) -> List[ConsumerModel]:
	result : List[ConsumerModel] = []

	# process devices

	for device in devices:
		result.append(
		{
			'consumer': 'razer_chroma',
			'type': 'device',
			'name': device.name,
			'active': set_device(device, color.get_by_status(status)),
			'status': status
		})
	return result


def set_device(device : Any, color_config : ColorConfigModel) -> bool:
	if device.has('brightness'):
		device.brightness = color_config['brightness'][0]
	if device.fx.has('static'):
		return device.fx.static(color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2])
	return use_effect(device, color_config, 'static')


def use_effect(device : Any, color_config : ColorConfigModel, effect_name : str) -> bool:
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
			effect_state = effect_function(color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2]) or effect_state
	return effect_state
