import atexit
import copy
from functools import partial
from typing import List

from chroma_feedback import color, helper, reporter
from chroma_feedback.types import ColorConfig, Consumer, Light, ProducerReport, Status
from .api import get_api

LIGHTS : List[Light] = []


def get_lights(bridge_ip : str) -> List[Light]:
	global LIGHTS

	if not LIGHTS:
		LIGHTS = get_api(bridge_ip).get_light_objects()
	return LIGHTS


def filter_lights(lights : List[Light], light_ids : List[str]) -> List[Light]:
	if light_ids:
		for light in copy.copy(lights):
			if light._get('uniqueid') not in light_ids:
				lights.remove(light)
	return lights


def process_lights(lights : List[Light], producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for light in lights:
		set_light(light, color.get_by_status(status))
		if helper.has_argument('-b') or helper.has_argument('--background-run'):
			register_reset_light(light)
		result.append(
		{
			'name': 'philips.hue',
			'type': 'light',
			'description': helper.create_description(light.name, light._get('uniqueid')),
			'status': status
		})
	return result


def set_light(light : Light, color_config : ColorConfig) -> None:
	get_api(None).set_light(light.name,
	{
		'hue': color_config.get('hue'),
		'sat': color_config.get('saturation')[1],
		'bri': color_config.get('brightness')[1],
		'on': True,
		'alert': 'none'
	})


def register_reset_light(light : Light) -> None:
	atexit.register(partial(get_api(None).set_light, light.name,
	{
		'on': False
	}))
