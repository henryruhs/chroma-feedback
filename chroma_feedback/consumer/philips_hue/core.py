import copy
import requests
from chroma_feedback import color, helper, wording
from .factory import api_factory

args = None
api = None


def init(program):
	global args

	if not args:
		ip = None

		if not helper.has_argument('--philips-hue-ip'):
			ip = discover_bridge_ip()
		if ip:
			program.add_argument('--philips-hue-ip', default = ip)
		else:
			program.add_argument('--philips-hue-ip', required = True)
		program.add_argument('--philips-hue-light', action = 'append')
		program.add_argument('--philips-hue-group', action = 'append')
	args = program.parse_known_args()[0]


def run(status):
	global api

	if not api:
		api = api_factory(args.philips_hue_ip)

	# use groups

	if args.philips_hue_group:
		groups = get_groups(api.get_group(), args.philips_hue_group)

		if not groups:
			exit(wording.get('group_no') + wording.get('exclamation_mark'))
		return process_groups(status, groups)

	# use lights

	lights = get_lights(api.get_light_objects(), args.philips_hue_light)

	if not lights:
		exit(wording.get('light_no') + wording.get('exclamation_mark'))
	return process_lights(status, lights)


def get_lights(lights, light_names):
	if light_names:
		for light in copy.copy(lights):
			if light.name not in light_names:
				lights.remove(light)
	return lights


def get_groups(groups, group_names):
	if group_names:
		for group in copy.copy(groups):
			group_name = groups[group]['name']

			if group_name not in group_names:
				del groups[group]
	return groups


def process_lights(status, lights):
	result = []

	# process lights

	for light in lights:
		if status == 'passed':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': light.name,
				'active': static_light(light.name, color.get_passed_hue()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': light.name,
				'active': static_light(light.name, color.get_process_hue()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': light.name,
				'active': pulsate_light(light.name, color.get_errored_hue()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': light.name,
				'active': pulsate_light(light.name, color.get_failed_hue()),
				'status': status
			})
	return result


def process_groups(status, groups):
	result = []

	# process groups

	for group in groups:
		group_name = groups[group]['name']

		if status == 'passed':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': group_name,
				'active': static_group(group_name, color.get_passed_hue()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': group_name,
				'active': static_group(group_name, color.get_process_hue()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': group_name,
				'active': pulsate_group(group_name, color.get_errored_hue()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': group_name,
				'active': pulsate_group(group_name, color.get_failed_hue()),
				'status': status
			})
	return result


def static_light(light_name, state):
	return api is not None and api.set_light(light_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'],
		'alert': 'none'
	}) is not None


def pulsate_light(light_name, state):
	return api is not None and api.set_light(light_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'],
		'alert': 'lselect'
	}) is not None


def static_group(group_name, state):
	return api is not None and api.set_group(group_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'],
		'alert': 'none'
	}) is not None


def pulsate_group(group_name, state):
	return api is not None and api.set_group(group_name,
	{
		'hue': state['hue'],
		'sat': state['saturation'],
		'alert': 'lselect'
	}) is not None


def discover_bridge_ip():
	response = requests.get('https://discovery.meethue.com')

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if data and data[0] and 'internalipaddress' in data[0]:
			return data[0]['internalipaddress']
	return None
