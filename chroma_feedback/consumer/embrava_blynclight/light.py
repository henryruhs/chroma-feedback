from typing import Any, List
import copy
from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status


def filter_lights(lights : Any, light_ids : List[str]) -> Any:
	if light_ids:
		for light in copy.copy(lights):
			if get_hud_id(light) not in light_ids:
				lights.remove(light)
	return lights


def get_hud_id(light : Any) -> str:
	return str(light.info['path'], 'utf-8')


def process_lights(lights : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process lights

	for light in lights:
		if set_light(light, color.get_by_status(status)):
			result.append(
			{
				'name': 'embrava_blynclight',
				'type': 'light',
				'description': light.info['product_string'] + ' [' + get_hud_id(light) + ']',
				'status': status
			})
	return result


def set_light(light : Any, color_config : Color) -> bool:
	light.on(tuple(color_config['rgb']))
	return light.is_on is True

