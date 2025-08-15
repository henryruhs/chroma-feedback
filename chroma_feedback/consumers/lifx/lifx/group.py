import atexit
from functools import partial
from typing import List, Optional

from chroma_feedback import color, helper, reporter
from chroma_feedback.types import ColorConfig, Consumer, Group, ProducerReport, Status
from .api import get_api

GROUPS : List[Group] = []


def get_groups(group_names : List[str]) -> List[Group]:
	global GROUPS

	if not GROUPS:
		if group_names:
			for group_name in group_names:
				group = get_api().get_devices_by_group(group_name)

				if group.get_device_list():
					GROUPS.append(group)
	return GROUPS


def get_group_name(group : Group) -> Optional[str]:
	for device in group.get_device_list():
		return device.get_group_label()
	return None


def process_groups(groups : List[Group], producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for group in groups:
		set_group(group, color.get_by_status(status))
		if helper.has_argument('-b') or helper.has_argument('--background-run'):
			register_reset_group(group)
		result.append(
		{
			'name': 'lifx',
			'type': 'group',
			'description': get_group_name(group),
			'status': status
		})
	return result


def set_group(group : Group, color_config : ColorConfig) -> None:
	group.set_power('on')
	group.set_color(
	[
		color_config.get('hue'),
		color_config.get('saturation')[2],
		color_config.get('brightness')[2],
		color_config.get('kelvin')
	])


def register_reset_group(group : Group) -> None:
	atexit.register(partial(group.set_power, 'off'))
