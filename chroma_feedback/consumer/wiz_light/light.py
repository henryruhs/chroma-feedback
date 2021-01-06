import asyncio
from typing import Any, Dict, List
from chroma_feedback import color
from .api import get_api, get_builder


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
				'name': light,
				'active': static_light(light, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'wiz_light',
				'type': 'light',
				'name': light,
				'active': static_light(light, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'wiz_light',
				'type': 'light',
				'name': light,
				'active': static_light(light, color.get_failed()),
				'status': status
			})
	return result


def get_light_name(light : Any) -> str:
	loop = asyncio.get_event_loop()
	config = loop.run_until_complete(light.getBulbConfig())
	if 'result' in config and 'moduleName' in config['result']:
		return config['result']['moduleName']
	return 'unknown'


def static_light(light : Any, state : Dict[str, Any]) -> bool:
	builder = get_builder()
	loop = asyncio.get_event_loop()
	loop.run_until_complete(light.turn_on(builder(rgb = state['rgb'])))
	return loop.close() is None
