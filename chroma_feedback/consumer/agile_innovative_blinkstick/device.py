from typing import Any, Dict, List
import copy

from chroma_feedback import color


def get_devices(devices : Any, device_names : List[str]) -> Any:
	if device_names:
		for device in copy.copy(devices):
			if device.get_serial() not in device_names:
				devices.remove(device)
	return devices


def process_devices(devices : Any, status : str) -> List[Dict[str, Any]]:
	result = []

	# process devices

	for device in devices:
		if status == 'passed':
			result.append(
			{
				'consumer': 'agile_innovative_blinkstick',
				'type': 'device',
				'name': device.get_serial(),
				'active': static_device(device, color.get_passed()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'agile_innovative_blinkstick',
				'type': 'device',
				'name': device.get_serial(),
				'active': static_device(device, color.get_process()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'agile_innovative_blinkstick',
				'type': 'device',
				'name': device.get_serial(),
				'active': static_device(device, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'agile_innovative_blinkstick',
				'type': 'device',
				'name': device.get_serial(),
				'active': static_device(device, color.get_failed()),
				'status': status
			})
	return result


def static_device(device : Any, state : Dict[str, Any]) -> bool:
	try:
		return device.set_color(red = state['rgb'][0], green = state['rgb'][1], blue = state['rgb'][2]) is None
	except OSError:
		return False
