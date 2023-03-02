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
		LIGHTS = get_api().all_lights()
	return LIGHTS


def filter_lights(lights : Any, light_ids : List[str]) -> Any:
	if light_ids:
		for light in copy.copy(lights):
			if light.path not in light_ids:
				lights.remove(light)
	return lights


def process_lights(lights : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	for light in lights:
		if set_light(light, color.get_by_status(status)):
			if helper.has_argument('-b') or helper.has_argument('--background-run'):
				register_reset_light(light)
			result.append(
			{
				'name': 'muteme.muteme_mini',
				'type': 'light',
				'description': helper.create_description(light.info['product_string'], light.path),
				'status': status
			})
	return result


def set_light(light : Any, color_config : Color) -> bool:
	light.on(tuple(color_config['rgb']))
	return light.is_on


def register_reset_light(light : Any) -> None:
	atexit.register(lambda: light.off())
