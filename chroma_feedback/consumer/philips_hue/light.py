import copy

from chroma_feedback import color
from .api import get_api


def get_lights(lights, light_names):
	if light_names:
		for light in copy.copy(lights):
			if light.name not in light_names:
				lights.remove(light)
	return lights


def process_lights(status, lights):
	result = []

	# process lights

	for light in lights:
		if status == 'passed':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'light',
				'name': light.name,
				'active': static_light(light.name, color.get_passed_hue()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'light',
				'name': light.name,
				'active': static_light(light.name, color.get_process_hue()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'light',
				'name': light.name,
				'active': pulsate_light(light.name, color.get_errored_hue()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'light',
				'name': light.name,
				'active': pulsate_light(light.name, color.get_failed_hue()),
				'status': status
			})
	return result


def static_light(light_name, state):
	api = get_api(None)

	return api is not None and api.set_light(light_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'],
		'alert': 'none'
	}) is not None


def pulsate_light(light_name, state):
	api = get_api(None)

	return api is not None and api.set_light(light_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'],
		'alert': 'lselect'
	}) is not None
