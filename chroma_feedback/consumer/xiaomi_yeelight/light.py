from chroma_feedback import color
from .api import get_api


def get_lights(ips):
	lights = []

	for ip in ips:
		lights.append(get_api(ip))
	return lights


def process_lights(status, lights):
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
		if status == 'process':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_process()),
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


def static_light(light, state):
	return light.turn_on() == 'ok' and light.set_rgb(state['rgb']['red'], state['rgb']['green'], state['rgb']['blue']) == 'ok'
