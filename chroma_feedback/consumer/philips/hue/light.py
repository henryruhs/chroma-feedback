import atexit
import copy
from typing import Any, List

from chroma_feedback import color, helper, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api

LIGHTS = None


def get_lights(bridge_ip : str) -> Any:
	global LIGHTS

	if not LIGHTS:
		LIGHTS = get_api(bridge_ip).get_light_objects()
	return LIGHTS


def filter_lights(lights : Any, light_ids : List[str]) -> Any:
	if light_ids:
		for light in copy.copy(lights):
			if light._get('uniqueid') not in light_ids:
				lights.remove(light)
	return lights


def process_lights(lights : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for light in lights:
		set_light(light, color.get_by_status(status))
		register_reset_light(light)
		result.append(
		{
			'name': 'philips.hue',
			'type': 'light',
			'description': helper.create_description(light.name, light._get('uniqueid')),
			'status': status
		})
	return result


def set_light(light: Any, color_config : Color) -> None:
	get_api(None).set_light(light.name,
	{
		'hue': color_config['hue'],
		'sat': color_config['saturation'][1],
		'bri': color_config['brightness'][1],
		'on': True,
		'alert': 'none'
	})


def register_reset_light(light: Any) -> None:
	atexit.register(lambda: get_api(None).set_light(light.name,
	{
		'on': False
	}))
