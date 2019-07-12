import requests
from chroma_feedback import helper, wording
from .factory import bridge_factory

args = None
bridge = None


def init(program):
	global args

	if not args:
		ip = None

		if not helper.has_argument('--philips-hue-ip'):
			ip = discover_ip()
		if ip:
			program.add_argument('--philips-hue-ip', default = ip)
		else:
			program.add_argument('--philips-hue-ip', required = True)
		program.add_argument('--philips-hue-group', action = 'append')
	args = program.parse_known_args()[0]


def run(status):
	global bridge

	if not bridge:
		bridge = bridge_factory(args.philips_hue_ip)
	groups = bridge.get_group()

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
		group_name = groups[group]['name']

		if status == 'passed':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': group_name,
				'active': static(group_name,
				{
					'hue': 26000,
					'sat': 255
				}),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': group_name,
				'active': static(group_name,
				{
					'hue': 10000,
					'sat': 255
				}),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': group_name,
				'active': pulsate(group_name,
				{
					'hue': 10000,
					'sat': 0
				}),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'philips_hue',
				'name': group_name,
				'active': pulsate(group_name,
				{
					'hue': 0,
					'sat': 255
				}),
				'status': status
			})
	return result


def static(group, state):
	return bridge is not None and bridge.set_group(group,
	{
		'hue': state['hue'],
		'sat': state['sat'],
		'on': True,
		'bri': 255,
		'alert': 'none'
	}) is not None


def pulsate(group, state):
	return bridge is not None and bridge.set_group(group,
	{
		'hue': state['hue'],
		'sat': state['sat'],
		'on': True,
		'bri': 255,
		'alert': 'lselect'
	}) is not None


def discover_ip():
	response = requests.get('https://discovery.meethue.com')

	# process response

	if response and response.status_code == 200:
		data = response.json()

		if data and data[0] and 'internalipaddress' in data[0]:
			return data[0]['internalipaddress']
	return None
