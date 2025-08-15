import atexit
import copy
from functools import partial
from typing import List

from chroma_feedback import color, helper, reporter
from chroma_feedback.types import ColorConfig, Consumer, Light, ProducerReport, Status
from .api import get_api

LIGHTS : List[Light] = []


def get_lights() -> List[Light]:
	global LIGHTS

	if not LIGHTS:
		LIGHTS = get_api().get_lights()
	return LIGHTS


def filter_lights(lights : List[Light], light_ips : List[str]) -> List[Light]:
	if light_ips:
		for light in copy.copy(lights):
			if light.get_ip_addr() not in light_ips:
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
			'name': 'lifx',
			'type': 'light',
			'description': helper.create_description(light.get_label(), light.get_ip_addr()),
			'status': status
		})
	return result


def set_light(light : Light, color_config : ColorConfig) -> None:
	light.set_power('on')
	light.set_color(
	[
		color_config.get('hue'),
		color_config.get('saturation')[2],
		color_config.get('brightness')[2],
		color_config.get('kelvin')
	])


def register_reset_light(light : Light) -> None:
	atexit.register(partial(light.set_power, 'off'))
