import json
import requests
from src import wording

args = None


def init(program):
	global args

	program.add_argument('--philips-hue-host', required = True)
	program.add_argument('--philips-hue-user', required = True)
	program.add_argument('--philips-hue-group', action = 'append', required = True)
	args = program.parse_known_args()[0]


def run(status):
	groups = args.philips_hue_group

	return process(status, groups)


def process(status, groups):
	message = []

	# process groups

	for group in groups:
		if status == 'passed' and static(group, 25500):
			message.append(wording.get('setting_passed').format(group) + wording.get('point'))
		if status == 'process' and static(group, 12500):
			message.append(wording.get('setting_process').format(group) + wording.get('point'))
		if status == 'errored' and pulsate(group, 34000):
			message.append(wording.get('setting_errored').format(group) + wording.get('point'))
		if status == 'failed' and pulsate(group, 0):
			message.append(wording.get('setting_failed').format(group) + wording.get('point'))
	return\
	{
		'message': message
	}


def static(group, hue):
	return update(group,
	{
		'hue': hue,
		'on': True,
		'bri': 255,
		'alert': 'none'
	})


def pulsate(group, hue):
	return update(group,
	 {
		'hue': hue,
		'on': True,
		'bri': 255,
		'alert': 'lselect'
	})


def update(group, data):
	response = None
	host = args.philips_hue_host
	user = args.philips_hue_user
	if host and user:
		response = requests.put(host + '/api/' + user + '/groups/' + group + '/action', data = json.dumps(data))

	# process response

	if response and response.status_code == 200:
		return True
	return False
