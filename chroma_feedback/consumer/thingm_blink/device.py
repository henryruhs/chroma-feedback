from typing import Any, Dict, List
import copy
from chroma_feedback import color
from .api import api_factory


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
				'active': static_device(device, color.get_passed()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'thingm_blink',
				'type': 'device',
				'name': device,
				'active': static_device(device, color.get_process()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'thingm_blink',
				'type': 'device',
				'name': device,
				'active': static_device(device, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'thingm_blink',
				'type': 'device',
				'name': device,
				'active': static_device(device, color.get_failed()),
				'status': status
			})
	return result


def static_device(device : Any, state : Dict[str, Any]) -> bool:
	api = api_factory(device)

	return api is not None and api.fade_to_rgb(100, state['rgb'][0], state['rgb'][1], state['rgb'][2]) is None
