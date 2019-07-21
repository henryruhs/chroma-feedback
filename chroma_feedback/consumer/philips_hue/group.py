import copy

from chroma_feedback import color
from .api import get_api


def get_groups(groups, group_names):
	if group_names:
		for group in copy.copy(groups):
			group_name = groups[group]['name']

			if group_name not in group_names:
				del groups[group]
	return groups


def process_groups(status, groups):
	result = []

	# process groups

	for group in groups:
		group_name = groups[group]['name']

		if status == 'passed':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'group',
				'name': group_name,
				'active': static_group(group_name, color.get_passed_hue()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'group',
				'name': group_name,
				'active': static_group(group_name, color.get_process_hue()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'group',
				'name': group_name,
				'active': pulsate_group(group_name, color.get_errored_hue()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'group',
				'name': group_name,
				'active': pulsate_group(group_name, color.get_failed_hue()),
				'status': status
			})
	return result


def static_group(group_name, state):
	api = get_api(None)

	return api is not None and api.set_group(group_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'],
		'alert': 'none'
	}) is not None


def pulsate_group(group_name, state):
	api = get_api(None)

	return api is not None and api.set_group(group_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'],
		'alert': 'lselect'
	}) is not None