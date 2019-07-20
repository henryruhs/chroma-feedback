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
				'active': static(light, color.get_passed_hue()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'light',
				'name': light_name,
				'active': static(light, color.get_process_hue()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'light',
				'name': light_name,
				'active': static(light, color.get_errored_hue()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'light',
				'name': light_name,
				'active': static(light, color.get_failed_hue()),
				'status': status
			})
	return result


def static(light, state):
	return light.set_hue(state['hue']) is None and light.set_saturation(state['saturation']) is None
