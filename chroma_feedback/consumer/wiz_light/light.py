from typing import Any, Dict, List
from chroma_feedback import color
from .api import get_api, get_loop, get_builder


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
				'consumer': 'wiz_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'wiz_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'wiz_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'wiz_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_failed()),
				'status': status
			})
	return result


def get_light_name(light : Any) -> str:
	loop = get_loop()
	config = loop.run_until_complete(light.get_bulbtype())
	return config.name


def static_light(light : Any, color_config : Dict[str, Any]) -> bool:
	loop = get_loop()
	builder = get_builder()
	loop.run_until_complete(light.turn_on(builder(rgb = color_config['rgb'])))
	return loop.is_closed() is False
