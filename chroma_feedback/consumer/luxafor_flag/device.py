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
				'consumer': 'luxaflor_flag',
				'type': 'device',
				'name': device.name,
				'active': static_device(device, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'luxaflor_flag',
				'type': 'device',
				'name': device.name,
				'active': static_device(device, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'luxaflor_flag',
				'type': 'device',
				'name': device.name,
				'active': static_device(device, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'luxaflor_flag',
				'type': 'device',
				'name': device.name,
				'active': static_device(device, color.get_failed()),
				'status': status
			})
	return result


def static_device(device : Any, color_config : Dict[str, Any]) -> bool:
	return device.on((color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2])) is None
