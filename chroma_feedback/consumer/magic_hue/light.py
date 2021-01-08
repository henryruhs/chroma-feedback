from typing import Any, Dict, List
from chroma_feedback import color
from .api import get_api, get_modes


def get_lights(ips : List[str]) -> List[Dict[str, Any]]:
	lights = []

	for ip in ips:
		lights.append(get_api(ip))
	return lights


def process_lights(lights : Any, status : str) -> List[Dict[str, Any]]:
	result = []

	# process lights

	for light in lights:
		if status == 'passed':
			result.append(
			{
				'consumer': 'magic_hue',
				'type': 'light',
				'name': light.name,
				'active': static_light(light, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'magic_hue',
				'type': 'light',
				'name': light.name,
				'active': static_light(light, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'magic_hue',
				'type': 'light',
				'name': light.name,
				'active': pulsate_light(light, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'magic_hue',
				'type': 'light',
				'name': light.name,
				'active': pulsate_light(light, color.get_failed()),
				'status': status
			})
	return result


def static_light(light : Any, color_config : Dict[str, Any]) -> bool:
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


def pulsate_light(light : Any, color_config : Dict[str, Any]) -> bool:
	modes = get_modes()

	if modes:
		light.mode = modes.CustomMode(
			mode = modes.MODE_GRADUALLY,
			speed = 1,
			colors =\
			[
				color_config['rgb'],
				(0, 0, 0)
			]
		)
	return light.update_status() is None
