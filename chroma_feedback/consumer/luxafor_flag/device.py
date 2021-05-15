from typing import Any, Dict, List
import copy
from chroma_feedback import color


def get_devices(devices : Any, device_serials : List[str]) -> Any:
	if device_serials:
		for device in copy.copy(devices):
			device_serial = device.info['serial_number']

			if device_serial not in device_serials:
				devices.remove(device)
	return devices


def process_devices(devices : Any, status : str) -> List[Dict[str, Any]]:
	result = []

	# process devices

	for device in devices:
		device_name = device.info['product_string']
		device_serial = device.info['serial_number']

		if status == 'passed':
			result.append(
			{
				'consumer': 'luxafor_flag',
				'type': 'device',
				'name': device_name,
				'serial': device_serial,
				'active': static_device(device, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'luxafor_flag',
				'type': 'device',
				'name': device_name,
				'serial': device_serial,
				'active': static_device(device, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'luxafor_flag',
				'type': 'device',
				'name': device_name,
				'serial': device_serial,
				'active': static_device(device, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'luxafor_flag',
				'type': 'device',
				'name': device_name,
				'serial': device_serial,
				'active': static_device(device, color.get_failed()),
				'status': status
			})
	return result


def static_device(device : Any, color_config : Dict[str, Any]) -> bool:
	return device.on((color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2])) is None
