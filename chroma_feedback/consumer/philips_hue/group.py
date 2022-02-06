import copy
from typing import Any, List

from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api

GROUPS = None


def get_groups(bridge_ip : str) -> Any:
	global GROUPS

	if not GROUPS:
		GROUPS = get_api(bridge_ip).get_group()
	return GROUPS


def filter_groups(groups : Any, group_names : List[str]) -> Any:
	if group_names:
		for index in copy.copy(groups):
			if groups[index]['name'] not in group_names:
				del groups[index]
	return groups


def process_groups(groups : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process groups

	for index in groups:
		set_group(groups[index]['name'], color.get_by_status(status))
		result.append(
		{
			'name': 'philips_hue',
			'type': 'group',
			'description': groups[index]['name'],
			'status': status
		})
	return result


def set_group(group_name : str, color_config : Color) -> None:
	get_api(None).set_group(group_name,
	{
		'hue': color_config['hue'],
		'sat': color_config['saturation'][1],
		'bri': color_config['brightness'][1],
		'on': True,
		'alert': 'none'
	})
