from chroma_feedback import color
from .api import get_api


def get_groups(group_names):
	api = get_api()
	groups = []

	if group_names:
		for group_name in group_names:
			groups.append(api.get_devices_by_group(group_name))
	return groups


def get_group_name(group):
	for device in group.get_device_list():
		return device.get_group_label()


def process_groups(status, groups):
	result = []

	# process groups

	for group in groups:
		group_name = get_group_name(group)

		if status == 'passed':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'group',
				'name': group_name,
				'active': static_group(group, color.get_passed_hue()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'group',
				'name': group_name,
				'active': static_group(group, color.get_process_hue()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'group',
				'name': group_name,
				'active': static_group(group, color.get_errored_hue()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'group',
				'name': group_name,
				'active': static_group(group, color.get_failed_hue()),
				'status': status
			})
	return result


def static_group(group, state):
	return group.set_hue(state['hue']) is None and group.set_saturation(state['saturation']) is None
