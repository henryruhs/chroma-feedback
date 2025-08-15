import atexit
from typing import List

from chroma_feedback import color, helper, reporter
from chroma_feedback.types import ColorConfig, Consumer, Light, ProducerReport, Status
from .api import get_api

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
		if set_light(light, color.get_by_status(status)):
			if helper.has_argument('-b') or helper.has_argument('--background-run'):
				register_reset_light(light)
			result.append(
			{
				'name': 'nanoleaf',
				'type': 'light',
				'description': helper.create_description(light.get_name(), light.ip),
				'status': status
			})
	return result


def set_light(light : Light, color_config : ColorConfig) -> bool:
	return light.set_color(color_config.get('rgb'))


def register_reset_light(light : Light) -> None:
	atexit.register(light.power_off)
