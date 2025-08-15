import atexit
import copy
from functools import partial
from typing import List

from chroma_feedback import color, helper, reporter
from chroma_feedback.types import ColorConfig, Consumer, Device, ProducerReport, Status
from .api import get_api

DEVICES : List[Device] = []


def get_devices() -> List[Device]:
	global DEVICES

	if not DEVICES:
		DEVICES = get_api().devices
	return DEVICES


def filter_devices(devices : List[Device], device_serials : List[str]) -> List[Device]:
	if device_serials:
		for device in copy.copy(devices):
			if device.serial not in device_serials:
				devices.remove(device)
	return devices


def process_devices(devices : List[Device], producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for device in devices:
		if set_device(device, color.get_by_status(status)):
			if helper.has_argument('-b') or helper.has_argument('--background-run'):
				register_reset_device(device)
			result.append(
			{
				'name': 'razer.chroma',
				'type': 'device',
				'description': helper.create_description(device.name, device.serial),
				'status': status
			})
	return result


def set_device(device : Device, color_config : ColorConfig) -> bool:
	if device.has('brightness'):
		device.brightness = color_config.get('brightness')[0]
	if device.fx.has('static'):
		return device.fx.static(*color_config.get('rgb'))
	return set_misc(device, color_config)


def set_misc(device : Device, color_config : ColorConfig) -> bool:
	state = False
	parts =\
	{
		'logo': 'logo',
		'scroll': 'scroll_wheel',
		'left': 'left',
		'right': 'right',
		'charging': 'charging',
		'fast_charging': 'fast_charging',
		'fully_charged': 'fully_charged',
		'backlight': 'backlight'
	}

	for part_key, part_value in parts.items():
		if device.fx.has(part_key + '_static'):
			function = getattr(getattr(device.fx.misc, part_value), 'static')
			state = function(*color_config.get('rgb')) or state
	return state


def register_reset_device(device : Device) -> None:
	atexit.register(partial(set_device, device, color.get_reset()))
