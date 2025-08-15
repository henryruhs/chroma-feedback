import atexit
from functools import partial
from typing import List

from chroma_feedback import color, helper, reporter
from chroma_feedback.types import ColorConfig, Consumer, Light, ProducerReport, Status
from .api import get_api, get_builder

LIGHTS : List[Light] = []


def get_lights(light_ips : List[str]) -> List[Light]:
	global LIGHTS

	if not LIGHTS:
		for light_ip in light_ips:
			LIGHTS.append(get_api(light_ip))
	return LIGHTS


def process_lights(lights : List[Light], producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for light in lights:
		set_light(light, color.get_by_status(status))
		if helper.has_argument('-b') or helper.has_argument('--background-run'):
			register_reset_light(light)
		result.append(
		{
			'name': 'signify.wiz',
			'type': 'light',
			'description': helper.create_description(get_light_name(light), light.ip),
			'status': status
		})
	return result


def get_light_name(light : Light) -> str:
	return light.loop.run_until_complete(light.get_bulbtype()).name


def set_light(light : Light, color_config : ColorConfig) -> None:
	builder = get_builder()
	light.loop.run_until_complete(light.turn_on(builder(rgb = color_config.get('rgb'))))


def register_reset_light(light : Light) -> None:
	atexit.register(partial(light.loop.run_until_complete, light.turn_off()))
