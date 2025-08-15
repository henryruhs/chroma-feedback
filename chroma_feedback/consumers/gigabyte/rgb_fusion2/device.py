import atexit
from functools import partial
from typing import List

from chroma_feedback import color, helper, reporter
from chroma_feedback.types import ColorConfig, Consumer, Device, ProducerReport, Status
from .api import get_api

DEVICES : List[Device] = []


def get_devices() -> List[Device]:
	global DEVICES

	if not DEVICES:
		DEVICES = get_api().find_supported_devices()
	return DEVICES


def process_devices(devices : List[Device], producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for device in devices:
		set_device(device, color.get_by_status(status))
		if helper.has_argument('-b') or helper.has_argument('--background-run'):
			register_reset_device(device)
		result.append(
		{
			'name': 'gigabyte.rgb_fusion2',
			'type': 'device',
			'description': device.description,
			'status': status
		})
	return result


def set_device(device : Device, color_config : ColorConfig) -> None:
	with device.connect():
		device.set_color('sync', 'fixed',
		[
			tuple(color_config.get('rgb'))
		])


def register_reset_device(device : Device) -> None:
	atexit.register(partial(set_device, device, color.get_reset()))
