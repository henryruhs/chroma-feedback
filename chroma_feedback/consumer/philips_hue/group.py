from typing import List, Dict, Any
import copy
from chroma_feedback import color
from .api import get_api


def get_groups(groups : Any, group_names : List[str]) -> Any:
	if group_names:
		for group in copy.copy(groups):
			group_name = groups[group]['name']

			if group_name not in group_names:
				del groups[group]
	return groups


def process_groups(groups : Any, status : str) -> List[Dict[str, Any]]:
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
				'active': static_group(group_name, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'group',
				'name': group_name,
				'active': static_group(group_name, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'group',
				'name': group_name,
				'active': pulsate_group(group_name, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'philips_hue',
				'type': 'group',
				'name': group_name,
				'active': pulsate_group(group_name, color.get_failed()),
				'status': status
			})
	return result


def static_group(group_name : str, state : Dict[str, Any]) -> bool:
	api = get_api(None)

	return api is not None and api.set_group(group_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'][1],
		'bri': state['brightness'][1],
		'on': True,
		'alert': 'none'
	}) is not None


def pulsate_group(group_name : str, state : Dict[str, Any]) -> bool:
	api = get_api(None)

	return api is not None and api.set_group(group_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'][1],
		'bri': state['brightness'][1],
		'on': True,
		'alert': 'lselect'
	}) is not None
