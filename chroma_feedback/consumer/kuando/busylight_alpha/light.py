import atexit
import copy
from typing import List

from chroma_feedback import color, helper, reporter
from chroma_feedback.types import ColorConfig, Consumer, Light, ProducerReport, Status
from .api import get_api

LIGHTS : List[Light] = []


def get_lights() -> List[Light]:
	global LIGHTS

	if not LIGHTS:
		LIGHTS = get_api().all_lights()
	return LIGHTS


def filter_lights(lights : List[Light], light_ids : List[str]) -> List[Light]:
	if light_ids:
		for light in copy.copy(lights):
			if light.path not in light_ids:
				lights.remove(light)
	return lights


def process_lights(lights : List[Light], producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for light in lights:
		if set_light(light, color.get_by_status(status)):
			if helper.has_argument('-b') or helper.has_argument('--background-run'):
				register_reset_light(light)
			result.append(
			{
				'name': 'kuando.busylight_alpha',
				'type': 'light',
				'description': helper.create_description(light.info['product_string'], light.path),
				'status': status
			})
	return result


def set_light(light : Light, color_config : ColorConfig) -> bool:
	light.on(tuple(color_config.get('rgb')))
	return light.is_on


def register_reset_light(light : Light) -> None:
	atexit.register(light.off)
