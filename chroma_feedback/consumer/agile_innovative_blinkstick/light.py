import copy
from typing import Any, List
from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api

LIGHTS = None


def get_lights() -> Any:
	global LIGHTS

	if not LIGHTS:
		LIGHTS = get_api().all_lights()
	return LIGHTS


def filter_lights(lights : Any, light_serials : List[str]) -> Any:
	if light_serials:
		for light in copy.copy(lights):
			if light.info['serial_number'] not in light_serials:
				lights.remove(light)
	return lights


def process_lights(lights : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process lights

	for light in lights:
		if set_light(light, color.get_by_status(status)):
			result.append(
			{
				'name': 'agile_innovative_blinkstick',
				'type': 'light',
				'description': light.info['product_string'] + ' [' + light.info['serial_number'] + ']',
				'status': status
			})
	return result


def set_light(light : Any, color_config : Color) -> bool:
	light.on(tuple(color_config['rgb']))
	return light.is_on is True
