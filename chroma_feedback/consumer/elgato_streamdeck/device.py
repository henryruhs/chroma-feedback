from typing import Any, List
import copy
import webbrowser

from chroma_feedback import color, reporter
from chroma_feedback.typing import Consumer, Report, Status
from .api import get_pil_helper


def get_devices(devices : Any, device_names : List[str]) -> Any:
	if device_names:
		for device in copy.copy(devices):
			if device.id() not in device_names:
				devices.remove(device)
	return devices


def process_devices(devices : Any, producer_report : List[Report]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process device

	for device in devices:
		if set_device(device, producer_report):
			result.append(
			{
				'consumer': 'elgato_streamdeck',
				'type': 'device',
				'name': device.id(),
				'status': status
			})
	return result


def set_device(device : Any, producer_report : List[Report]) -> bool:
	device.open()

	# process producer

	for index, value in enumerate(producer_report):
		color_config = color.get_by_status(value['status'])

		if index < device.key_count():
			device.set_key_image(index, create_image(device, background = color_config['name']))
			if 'url' in value and value['url'] is not None:
				device.set_key_callback(lambda : webbrowser.open(value['url']))

	# close device

	device.close()
	return device.is_open() is False


def create_image(device : Any, background : str) -> Any:
	pil_helper = get_pil_helper()

	return pil_helper.to_native_format(device, pil_helper.create_image(device, background = background))
