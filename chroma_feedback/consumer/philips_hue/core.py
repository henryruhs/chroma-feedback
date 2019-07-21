import requests
from chroma_feedback import helper, wording
from .group import get_groups, process_groups
from .light import get_lights, process_lights
from .api import get_api

ARGS = None


def init(program):
	global ARGS

	if not ARGS:
		ip = None

		if not helper.has_argument('--philips-hue-ip'):
			ip = discover_ip()
		if ip:
			program.add_argument('--philips-hue-ip', default = ip)
		else:
			program.add_argument('--philips-hue-ip', required = True)
		program.add_argument('--philips-hue-light', action = 'append')
		program.add_argument('--philips-hue-group', action = 'append')
	ARGS = program.parse_known_args()[0]


def run(status):
	api = get_api(ARGS.philips_hue_ip)

	# use groups

	if ARGS.philips_hue_group:
		groups = get_groups(api.get_group(), ARGS.philips_hue_group)

		if not groups:
			exit(wording.get('group_no') + wording.get('exclamation_mark'))
		return process_groups(status, groups)

	# use lights

	lights = get_lights(api.get_light_objects(), ARGS.philips_hue_light)

	if not lights:
		exit(wording.get('light_no') + wording.get('exclamation_mark'))
	return process_lights(status, lights)


def discover_ip():
	response = requests.get('https://discovery.meethue.com')

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if data and data[0] and 'internalipaddress' in data[0]:
			return data[0]['internalipaddress']
	return None
