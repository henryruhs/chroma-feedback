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

		if status == 'passed':
			result.append(
			{
				'consumer': 'wiz_light',
				'type': 'light',
				'name': light.name,
				'active': static_light(light, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'wiz_light',
				'type': 'light',
				'name': light.name,
				'active': static_light(light, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'wiz_light',
				'type': 'light',
				'name': light.name,
				'active': pulsate_light(light, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'wiz_light',
				'type': 'light',
				'name': light.name,
				'active': pulsate_light(light, color.get_failed()),
				'status': status
			})
	return result


def static_light(light : Any, state : Dict[str, Any]) -> bool:
	print('static_light')


def pulsate_light(light : Any, state : Dict[str, Any]) -> bool:
	print('pulsate_light')
