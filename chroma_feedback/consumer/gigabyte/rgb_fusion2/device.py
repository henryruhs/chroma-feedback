import atexit
from typing import Any, List

from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api

DEVICES = None


def get_devices() -> Any:
	global DEVICES

	if not DEVICES:
		DEVICES = get_api().find_supported_devices()
	return DEVICES


def process_devices(devices : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for device in devices:
		set_device(device, color.get_by_status(status))
		register_reset_device(device)
		result.append(
		{
			'name': 'gigabyte.rgb_fusion2',
			'type': 'device',
			'description': device.description,
			'status': status
		})
	return result


def set_device(device : Any, color_config : Color) -> None:
	with device.connect():
		device.set_color('sync', 'fixed',
		[
			tuple(color_config['rgb'])
		])


def register_reset_device(device : Any) -> None:
	atexit.register(lambda: set_device(device, color.get_reset()))
