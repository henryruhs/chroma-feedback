from typing import Any, Dict, List
import copy
from chroma_feedback import color
from .api import get_api


def get_lights(lights : Any, light_names : List[str]) -> Any:
	if light_names:
		for light in copy.copy(lights):
			if light.name not in light_names:
				lights.remove(light)
	return lights


def process_lights(lights : Any, status : str) -> List[Dict[str, Any]]:
	result = []

	# process lights

	for light in lights:
		if status == 'passed':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'light',
				'name': light.name,
				'active': static_light(light.name, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'light',
				'name': light.name,
				'active': static_light(light.name, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'light',
				'name': light.name,
				'active': pulsate_light(light.name, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'light',
				'name': light.name,
				'active': pulsate_light(light.name, color.get_failed()),
				'status': status
			})
	return result


def static_light(light_name : str, state : Dict[str, Any]) -> bool:
	api = get_api(None)

	return api is not None and api.set_light(light_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'][1],
		'bri': state['brightness'][1],
		'on': True,
		'alert': 'none'
	}) is not None


def pulsate_light(light_name : str, state : Dict[str, Any]) -> bool:
	api = get_api(None)

	return api is not None and api.set_light(light_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'][1],
		'bri': state['brightness'][1],
		'on': True,
		'alert': 'lselect'
	}) is not None
