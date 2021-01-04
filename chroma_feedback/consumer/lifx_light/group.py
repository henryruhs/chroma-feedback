from typing import Any, Dict, List
from chroma_feedback import color
from .api import get_api


def get_groups(group_names : List[str]) -> List[Dict[str, Any]]:
	api = get_api()
	groups = []

	if group_names:
		for group_name in group_names:
			groups.append(api.get_devices_by_group(group_name))
	return groups


def get_group_name(group : Any) -> Any:
	for device in group.get_device_list():
		return device.get_group_label()


def process_groups(groups : Any, status : str) -> List[Dict[str, Any]]:
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
				'active': static_group(group, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'group',
				'name': group_name,
				'active': static_group(group, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'group',
				'name': group_name,
				'active': static_group(group, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'lifx_light',
				'type': 'group',
				'name': group_name,
				'active': static_group(group, color.get_failed()),
				'status': status
			})
	return result


def static_group(group : Any, state : Dict[str, Any]) -> bool:
	return group.set_power('on') is None and group.set_color(
	[
		state['hue'],
		state['saturation'][2],
		state['brightness'][2],
		state['kelvin']
	]) is None
