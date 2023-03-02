import atexit
import copy
from typing import Any, List

from chroma_feedback import color, helper, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api

LIGHTS = None


def get_lights() -> Any:
	global LIGHTS

	if not LIGHTS:
		LIGHTS = get_api().get_lights()
	return LIGHTS


def filter_lights(lights : Any, light_ips : List[str]) -> Any:
	if light_ips:
		for light in copy.copy(lights):
			if light.get_ip_addr() not in light_ips:
				lights.remove(light)
	return lights


def process_lights(lights : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
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


def set_light(light : Any, color_config : Color) -> None:
	light.set_power('on')
	light.set_color(
	[
		color_config['hue'],
		color_config['saturation'][2],
		color_config['brightness'][2],
		color_config['kelvin']
	])


def register_reset_light(light : Any) -> None:
	atexit.register(lambda: light.set_power('off'))
