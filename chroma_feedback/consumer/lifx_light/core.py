import copy
from chroma_feedback import color, wording
from .factory import api_factory

args = None
api = None


def init(program):
	global args

	if not args:
		program.add_argument('--lifx-light-light', action = 'append')
		program.add_argument('--lifx-light-group', action = 'append')
	args = program.parse_known_args()[0]


def run(status):
	global api

	if not api:
		api = api_factory()

	# use groups

	if args.lifx_light_group:
		groups = get_groups(args.lifx_light_group)

		if not groups:
			exit(wording.get('group_no') + wording.get('exclamation_mark'))
		return process_groups(status, groups)

	# use lights

	lights = get_lights(api.get_lights(), args.lifx_light_light)

	if not lights:
		exit(wording.get('light_no') + wording.get('exclamation_mark'))
	return process_lights(status, lights)


def get_lights(lights, light_names):
	if light_names:
		for light in copy.copy(lights):
			light_name = light.get_label()

			if light_name not in light_names:
				lights.remove(light)
	return lights


def get_groups(group_names):
	groups = []

	if group_names:
		for group_name in group_names:
			groups.append(api.get_devices_by_group(group_name))
	return groups


def process_lights(status, lights):
	result = []

	# process lights

	for light in lights:
		light_name = light.get_label()

		if status == 'passed':
			result.append(
			{
				'consumer': 'lifx_light',
				'name': light_name,
				'active': static_light(light, color.get_passed_hue()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'lifx_light',
				'name': light_name,
				'active': static_light(light, color.get_process_hue()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'lifx_light',
				'name': light_name,
				'active': static_light(light, color.get_errored_hue()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'lifx_light',
				'name': light_name,
				'active': static_light(light, color.get_failed_hue()),
				'status': status
			})
	return result


def process_groups(status, groups):
	result = []

	# process groups

	for group in groups:
		group_name = get_group_name(group)

		if status == 'passed':
			result.append(
			{
				'consumer': 'lifx_light',
				'name': group_name,
				'active': static_group(group, color.get_passed_hue()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'lifx_light',
				'name': group_name,
				'active': static_group(group, color.get_process_hue()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'lifx_light',
				'name': group_name,
				'active': static_group(group, color.get_errored_hue()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'lifx_light',
				'name': group_name,
				'active': static_group(group, color.get_failed_hue()),
				'status': status
			})
	return result


def get_group_name(group):
	for device in group.get_device_list():
		return device.get_group_label()


def static_light(light, state):
	return light.set_hue(state['hue']) is None and light.set_saturation(state['saturation']) is None


def static_group(group, state):
	return group.set_hue(state['hue']) is None and group.set_saturation(state['saturation']) is None
