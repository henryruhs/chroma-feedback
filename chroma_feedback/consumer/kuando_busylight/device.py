from typing import Any, List
import copy
from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status


def get_devices(devices : Any, device_names : List[str]) -> Any:
	if device_names:
		for device in copy.copy(devices):
			if device.info['product_string'] not in device_names:
				devices.remove(device)
	return devices


def process_devices(devices : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process devices

	for device in devices:
		if set_device(device, color.get_by_status(status)):
			result.append(
			{
				'consumer': 'kuando_busylight',
				'type': 'device',
				'name': device.info['product_string'],
				'status': status
			})
	return result


def set_device(device : Any, color_config : Color) -> bool:
	device.on(tuple(color_config['rgb']))
	return device.is_on() and device.is_animating()
