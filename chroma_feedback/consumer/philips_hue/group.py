from typing import List, Any
import copy

from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api


def get_groups(groups : Any, group_names : List[str]) -> Any:
	if group_names:
		for index in copy.copy(groups):
			if groups[index]['name'] not in group_names:
				del groups[index]
	return groups


def process_groups(groups : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status: Status = reporter.resolve_report_status(producer_report)

	# process groups

	for index in groups:
		if set_group(groups[index]['name'], color.get_by_status(status)):
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'group',
				'name': groups[index]['name'],
				'status': status
			})
	return result


def set_group(group_name : str, color_config : Color) -> bool:
	api = get_api(None)

	return api is not None and api.set_group(group_name,
	{
		'hue': color_config['hue'],
		'sat': color_config['saturation'][1],
		'bri': color_config['brightness'][1],
		'on': True,
		'alert': 'none'
	}) is not None
