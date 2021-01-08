from typing import Any, Dict, List
import copy
from chroma_feedback import color
from .api import get_api


def get_devices(devices : Any, device_names : List[str]) -> Any:
	if device_names:
		for device in copy.copy(devices):
			if device not in device_names:
				devices.remove(device)
	return devices


def process_devices(devices : Any, status : str) -> List[Dict[str, Any]]:
	result = []

	# process devices

	for device in devices:
		if status == 'passed':
			result.append(
			{
				'consumer': 'thingm_blink',
				'type': 'device',
				'name': device,
				'active': static_device(color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'thingm_blink',
				'type': 'device',
				'name': device,
				'active': static_device(color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'thingm_blink',
				'type': 'device',
				'name': device,
				'active': static_device(color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'thingm_blink',
				'type': 'device',
				'name': device,
				'active': static_device(color.get_failed()),
				'status': status
			})
	return result


def static_device(color_config : Dict[str, Any]) -> bool:
	api = get_api()

	return api is not None and api.fade_to_rgb(0, color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2]) is None
