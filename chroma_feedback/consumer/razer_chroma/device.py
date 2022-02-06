import copy
from typing import Any, List

from chroma_feedback import color, helper, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api

DEVICES = None


def get_devices() -> Any:
	global DEVICES

	if not DEVICES:
		DEVICES = get_api().devices
	return DEVICES


def filter_devices(devices : Any, device_serials : List[str]) -> Any:
	if device_serials:
		for device in copy.copy(devices):
			if device.serial not in device_serials:
				devices.remove(device)
	return devices


def process_devices(devices : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process devices

	for device in devices:
		if set_device(device, color.get_by_status(status)):
			result.append(
			{
				'name': 'razer_chroma',
				'type': 'device',
				'description': helper.create_description(device.name, device.serial),
				'status': status
			})
	return result


def set_device(device : Any, color_config : Color) -> bool:
	if device.has('brightness'):
		device.brightness = color_config['brightness'][0]
	if device.fx.has('static'):
		return device.fx.static(color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2])
	return use_effect(device, color_config, 'static')


def use_effect(device : Any, color_config : Color, effect_name : str) -> bool:
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
