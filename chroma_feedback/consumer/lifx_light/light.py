from typing import Any, List
import copy
from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status


def get_lights(lights : Any, light_names : List[str]) -> Any:
	if light_names:
		for light in copy.copy(lights):
			if light.get_label() not in light_names:
				lights.remove(light)
	return lights


def process_lights(lights : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process lights

	for light in lights:
		set_light(light, color.get_by_status(status))
		result.append(
		{
			'name': 'lifx_light',
			'type': 'light',
			'description': light.get_label(),
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
