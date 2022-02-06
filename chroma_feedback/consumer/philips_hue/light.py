import copy
from typing import Any, List

from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api


def filter_lights(lights : Any, light_names : List[str]) -> Any:
	if light_names:
		for light in copy.copy(lights):
			if light.name not in light_names:
				lights.remove(light)
	return lights


def process_lights(lights : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process lights

	for light in lights:
		if set_light(light.name, color.get_by_status(status)):
			result.append(
			{
				'name': 'philips_hue',
				'type': 'light',
				'description': light.name,
				'status': status
			})
	return result


def set_light(light_name : str, color_config : Color) -> bool:
	api = get_api(None)

	return api is not None and api.set_light(light_name,
	{
		'hue': color_config['hue'],
		'sat': color_config['saturation'][1],
		'bri': color_config['brightness'][1],
		'on': True,
		'alert': 'none'
	}) is not None
