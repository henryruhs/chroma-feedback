from typing import Any, List
import copy
from chroma_feedback import color, helper
from chroma_feedback.typing import Color, Consumer, Producer, Status


def get_devices(devices : Any, device_serials : List[str]) -> Any:
	if device_serials:
		for device in copy.copy(devices):
			if device.info['serial_number'] not in device_serials:
				devices.remove(device)
	return devices


def process_devices(devices : Any, producer_result : List[Producer]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = helper.resolve_producer_status(producer_result)

	# process devices

	for device in devices:
		result.append(
		{
			'consumer': 'agile_innovative_blinkstick',
			'type': 'device',
			'name': ' '.join([device.info['product_string'], device.info['serial_number']]),
			'active': set_device(device, color.get_by_status(status)),
			'status': status
		})
	return result


def set_device(device : Any, color_config : Color) -> bool:
	return device.on(tuple(color_config['rgb'])) is None
