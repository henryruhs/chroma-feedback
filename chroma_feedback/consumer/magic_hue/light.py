from typing import Any, List

from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api, get_modes


def get_lights(light_ips : List[str]) -> Any:
	lights = []

	for light_ip in light_ips:
		lights.append(get_api(light_ip))
	return lights


def process_lights(lights : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process lights

	for light in lights:
		set_light(light, color.get_by_status(status))
		result.append(
		{
			'name': 'magic_hue',
			'type': 'light',
			'description': light.description,
			'status': status
		})
	return result


def set_light(light : Any, color_config : Color) -> None:
	modes = get_modes()

	if modes:
		light.mode = modes.CustomMode(
			mode = modes.MODE_GRADUALLY,
			speed = 1,
			colors =\
			[
				color_config['rgb'],
				color_config['rgb']
			]
		)
	return light.update_status()
