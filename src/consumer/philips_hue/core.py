import json
import requests

args = None


def init(program):
	global args

	if not args:
		host = discover_host()

		if host:
			program.add_argument('--philips-hue-host', default = host)
		else:
			program.add_argument('--philips-hue-host', required = True)
		program.add_argument('--philips-hue-username', required = True)
		program.add_argument('--philips-hue-group', action = 'append', required = True)
	args = program.parse_known_args()[0]


def run(status):
	groups = args.philips_hue_group

	return process(status, groups)


def process(status, groups):
	result = []

	# process groups

	for group in groups:
		if status == 'passed':
			result.append({
				'consumer': 'philips_hue',
				'name': group,
				'active': static(group, 26000, 255),
				'status': status
			})
		if status == 'process':
			result.append({
				'consumer': 'philips_hue',
				'name': group,
				'active': static(group, 10000, 255),
				'status': status
			})
		if status == 'errored':
			result.append({
				'consumer': 'philips_hue',
				'name': group,
				'active': pulsate(group, 10000, 0),
				'status': status
			})
		if status == 'failed':
			result.append({
				'consumer': 'philips_hue',
				'name': group,
				'active': pulsate(group, 0, 255),
				'status': status
			})
	return result


def static(group, hue, sat):
	return update(group,
	{
		'hue': hue,
		'sat': sat,
		'on': True,
		'bri': 255,
		'alert': 'none'
	})


def pulsate(group, hue, sat):
	return update(group,
	 {
		'hue': hue,
		'sat': sat,
		'on': True,
		'bri': 255,
		'alert': 'lselect'
	})


def update(group, data):
	response = None
	host = args.philips_hue_host
	username = args.philips_hue_username

	if host and username:
		response = requests.put(host + '/api/' + username + '/groups/' + group + '/action', data = json.dumps(data))

	# process response

	if response and response.status_code == 200:
		return True
	return False


def discover_host():
	response = requests.get('https://discovery.meethue.com')

	# process response

	if response and response.status_code == 200:
		data = response.json()

		if 'internalipaddress' in data[0]:
			return 'http://' + data[0]['internalipaddress']
	return None
