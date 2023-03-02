import atexit
from typing import Any, List

from chroma_feedback import color, helper, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api

LIGHTS : List[Any] = []


def get_lights(light_ips : List[str]) -> List[Any]:
	global LIGHTS

	if not LIGHTS:
		for light_ip in light_ips:
			LIGHTS.append(get_api(light_ip))
	return LIGHTS


def process_lights(lights : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for light in lights:
		if set_light(light, color.get_by_status(status)):
			if helper.has_argument('-b') or helper.has_argument('--background-run'):
				register_reset_light(light)
			result.append(
			{
				'name': 'xiaomi.yeelight',
				'type': 'light',
				'description': helper.create_description(light.get_properties()['name'], light._ip),
				'status': status
			})
	return result


def set_light(light : Any, color_config : Color) -> bool:
	return light.turn_on() == 'ok' and light.set_rgb(*color_config['rgb']) == 'ok'


def register_reset_light(light : Any) -> None:
	atexit.register(lambda: light.turn_off())
