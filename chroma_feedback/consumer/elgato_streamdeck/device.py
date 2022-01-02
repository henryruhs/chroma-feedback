from typing import Any, List
import copy
from chroma_feedback import color, helper
from chroma_feedback.typing import Consumer, Producer, Status
from .api import get_pil_helper


def get_devices(devices : Any, device_names : List[str]) -> Any:
	if device_names:
		for device in copy.copy(devices):
			if device.id() not in device_names:
				devices.remove(device)
	return devices


def process_devices(devices : Any, producer_result : List[Producer]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = helper.resolve_producer_status(producer_result)

	# process device

	for device in devices:
		result.append(
		{
			'consumer': 'elgato_streamdeck',
			'type': 'device',
			'name': device.id(),
			'active': set_device(device, producer_result),
			'status': status
		})
	return result


def set_device(device : Any, producer_result : List[Producer]) -> bool:
	device.open()
	key_total = device.key_count()

	# process producer

	for producer_index, producer in enumerate(producer_result):
		color_config = color.get_by_status(producer['status'])

		if producer_index < key_total:
			device.set_key_image(producer_index, create_icon(device, background = color_config['name']))

	# process blank

	for blank_index in range(key_total):
		if blank_index > producer_index:
			device.set_key_image(blank_index, create_icon(device))

	device.__del__()
	return True


def create_icon(device : Any, background : str = None) -> Any:
	pil_helper = get_pil_helper()

	return pil_helper.to_native_format(device, pil_helper.create_image(device, background = background))
