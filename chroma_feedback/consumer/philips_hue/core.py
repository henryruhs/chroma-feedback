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
		program.add_argument('--philips-hue-group', action = 'append')
	args = program.parse_known_args()[0]


def run(status):
	global api

	if not api:
		api = api_factory(args.philips_hue_ip)
	groups = api.get_group()

	if args.philips_hue_group:
		for group in dict(groups):
			group_name = groups[group]['name']

			if group_name not in args.philips_hue_group:
				del groups[group]
	if not groups:
		exit(wording.get('group_no') + wording.get('exclamation_mark'))
	return process(status, groups)


def process(status, groups):
	result = []

	# process groups

	for group in groups:
		name = groups[group]['name']

		if status == 'passed':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': name,
				'active': static(name, color.get_passed_hue()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': name,
				'active': static(name, color.get_process_hue()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': name,
				'active': pulsate(name, color.get_errored_hue()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': name,
				'active': pulsate(name, color.get_failed_hue()),
				'status': status
			})
	return result


def static(group, state):
	return api is not None and api.set_group(group,
	{
		'hue': state['hue'],
		'sat': state['saturation'],
		'alert': 'none'
	}) is not None


def pulsate(group, state):
	return api is not None and api.set_group(group,
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
