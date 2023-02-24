import atexit
from typing import Any, List

from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api

GROUPS : List[Any] = []


def get_groups(group_names : List[str]) -> List[Any]:
	global GROUPS

	if not GROUPS:
		if group_names:
			for group_name in group_names:
				group = get_api().get_devices_by_group(group_name)

				if group.get_device_list():
					GROUPS.append(group)
	return GROUPS


def get_group_name(group : Any) -> Any:
	for device in group.get_device_list():
		return device.get_group_label()


def process_groups(groups : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for group in groups:
		set_group(group, color.get_by_status(status))
		register_reset_group(group)
		result.append(
		{
			'name': 'lifx',
			'type': 'group',
			'description': get_group_name(group),
			'status': status
		})
	return result


def set_group(group : Any, color_config : Color) -> None:
	group.set_power('on')
	group.set_color(
	[
		color_config['hue'],
		color_config['saturation'][2],
		color_config['brightness'][2],
		color_config['kelvin']
	])


def register_reset_group(group : Any) -> None:
	atexit.register(lambda: group.set_power('off'))
