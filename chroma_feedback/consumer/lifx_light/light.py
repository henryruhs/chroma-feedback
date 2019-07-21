import copy

from chroma_feedback import color


def get_lights(lights, light_names):
	if light_names:
		for light in copy.copy(lights):
			light_name = light.get_label()

			if light_name not in light_names:
				lights.remove(light)
	return lights


def process_lights(status, lights):
	result = []

	# process lights

	for light in lights:
		light_name = light.get_label()

		if status == 'passed':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_passed()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_process()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'light',
				'name': light_name,
				'active': static_light(light, color.get_failed()),
				'status': status
			})
	return result


def static_light(light, state):
	return light.set_power('on') is None and light.set_color(
	[
		state['hue'],
		state['saturation'][2],
		state['brightness'][2],
		state['kelvin']
	]) is None
