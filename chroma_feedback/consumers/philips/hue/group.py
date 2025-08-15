import atexit
import copy
from functools import partial
from typing import List

from chroma_feedback import color, helper, reporter
from chroma_feedback.types import ColorConfig, Consumer, Group, ProducerReport, Status
from .api import get_api

GROUPS : List[Group] = []


def get_groups(bridge_ip : str) -> List[Group]:
	global GROUPS

	if not GROUPS:
		GROUPS = get_api(bridge_ip).get_group()
	return GROUPS


def filter_groups(groups : List[Group], group_names : List[str]) -> List[Group]:
	if group_names:
		for index in copy.copy(groups):
			if groups[index]['name'] not in group_names:
				del groups[index]
	return groups


def process_groups(groups : List[Group], producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for index in groups:
		set_group(groups[index], color.get_by_status(status))
		if helper.has_argument('-b') or helper.has_argument('--background-run'):
			register_reset_group(groups[index])
		result.append(
		{
			'name': 'philips.hue',
			'type': 'group',
			'description': groups[index]['name'],
			'status': status
		})
	return result


def set_group(group : Group, color_config : ColorConfig) -> None:
	get_api(None).set_group(group['name'],
	{
		'hue': color_config.get('hue'),
		'sat': color_config.get('saturation')[1],
		'bri': color_config.get('brightness')[1],
		'on': True,
		'alert': 'none'
	})


def register_reset_group(group : Group) -> None:
	atexit.register(partial(get_api(None).set_group, group['name'],
	{
		'on': False
	}))
