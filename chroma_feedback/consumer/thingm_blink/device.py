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


def process_devices(devices : Any, status : str, *args : str, **kwargs : str) -> List[Dict[str, Any]]:
	result = []

	effect = kwargs.get('effect', 'default')

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
		if status == 'process':
			result.append(
			{
				'consumer': 'thingm_blink',
				'type': 'device',
				'name': device,
				'active': pulse_device(color.get_warning()) if effect == 'pulse' else static_device(color.get_process()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'thingm_blink',
				'type': 'device',
				'name': device,
				'active': pulse_device(color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'thingm_blink',
				'type': 'device',
				'name': device,
				'active': pulse_device(color.get_failed()),
				'status': status
			})
	return result


def static_device(state : Dict[str, Any]) -> bool:
	api = get_api()

	return api is not None and api.fade_to_rgb(0, state['rgb'][0], state['rgb'][1], state['rgb'][2]) is None

def pulse_device(state : Dict[str, Any]) -> bool:
	api = get_api()

	if api is not None:
		api.write_pattern_line(2000, 'black', 0)
		api.write_pattern_line(2000, state['name'],  1)
		return api.play(0,1,0) is None

	return False
