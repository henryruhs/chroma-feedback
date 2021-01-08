from typing import Any, Dict, List
from chroma_feedback import color
from .api import get_api


def get_lights(ips : List[str]) -> List[Dict[str, Any]]:
	lights = []

	for ip in ips:
		lights.append(get_api(ip))
	return lights


def process_lights(lights : Any, status : str) -> List[Dict[str, Any]]:
	result = []

	# process lights

	for light in lights:
		light_name = get_light_name(light)

		if status == 'passed':
			result.append(
			{
				'consumer': 'nanoleaf_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'nanoleaf_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'nanoleaf_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'nanoleaf_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_failed()),
				'status': status
			})
	return result


def get_light_name(light : Any) -> str:
	info = light.get_panel_info()
	if 'name' in info:
		return info['name']
	return 'unknown'


def static_light(light : Any, color_config : Dict[str, Any]) -> bool:
	return light.set_color(color_config['rgb'])
