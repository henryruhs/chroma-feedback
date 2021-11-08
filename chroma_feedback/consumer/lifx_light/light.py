from typing import Any, List
import copy
from chroma_feedback import color
from chroma_feedback.typing import Status, Consumer, Color


def get_lights(lights : Any, light_names : List[str]) -> Any:
	if light_names:
		for light in copy.copy(lights):
			if light.get_label() not in light_names:
				lights.remove(light)
	return lights


def process_lights(lights : Any, status : Status) -> List[Consumer]:
	result : List[Consumer] = []

	# process lights

	for light in lights:
		result.append(
		{
			'consumer': 'lifx_light',
			'type': 'light',
			'name': light.get_label(),
			'active': set_light(light, color.get_by_status(status)),
			'status': status
		})
	return result


def set_light(light : Any, color_config : Color) -> bool:
	return light.set_power('on') is None and light.set_color(
	[
		color_config['hue'],
		color_config['saturation'][2],
		color_config['brightness'][2],
		color_config['kelvin']
	]) is None
