from typing import Any, List
from chroma_feedback import color
from chroma_feedback.typing import Status, Consumer, Color
from .api import get_api, get_modes


def get_lights(ips : List[str]) -> Any:
	lights = []

	for ip in ips:
		lights.append(get_api(ip))
	return lights


def process_lights(lights : Any, status : Status) -> List[Consumer]:
	result : List[Consumer] = []

	# process lights

	for light in lights:
		result.append(
		{
			'consumer': 'magic_hue',
			'type': 'light',
			'name': light.name,
			'active': set_light(light, color.get_by_status(status)),
			'status': status
		})
	return result


def set_light(light : Any, color_config : Color) -> bool:
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
	return light.update_status() is None
