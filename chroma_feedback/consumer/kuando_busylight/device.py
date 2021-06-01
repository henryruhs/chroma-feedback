from typing import Any, Dict, List
import copy
from chroma_feedback import color
from chroma_feedback.typing import StatusType


def get_devices(devices : Any, device_names : List[str]) -> Any:
	if device_names:
		for device in copy.copy(devices):
			if device.info['product_string'] not in device_names:
				devices.remove(device)
	return devices


def process_devices(devices : Any, status : StatusType) -> List[Dict[str, Any]]:
	result = []

	# process devices

	for device in devices:
		result.append(
		{
			'consumer': 'kuando_busylight',
			'type': 'device',
			'name': device.info['product_string'],
			'active': set_device(device, color.get_by_status(status)),
			'status': status
		})
	return result


def set_device(device : Any, color_config : Dict[str, Any]) -> bool:
	return device.on(tuple(color_config['rgb'])) is None
