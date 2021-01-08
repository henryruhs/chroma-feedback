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
		light_name = light.get_properties()['name']

		if status == 'passed':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_failed()),
				'status': status
			})
	return result


def static_light(light : Any, color_config : Dict[str, Any]) -> bool:
	return light.turn_on() == 'ok' and light.set_rgb(color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2]) == 'ok'
