from typing import Any, Dict, List
from argparse import ArgumentParser
import socket
from chroma_feedback import helper, wording
from chroma_feedback.typing import StatusType
from .group import get_groups, process_groups
from .light import get_lights, process_lights
from .api import get_api

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		ip = None

		if not helper.has_argument('--philips-hue-ip'):
			ip = helper.get_first(discover_ips())
		if ip:
			program.add_argument('--philips-hue-ip', default = ip)
		else:
			program.add_argument('--philips-hue-ip', required = True)
		program.add_argument('--philips-hue-light', action = 'append')
		program.add_argument('--philips-hue-group', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(status : StatusType) -> List[Dict[str, Any]]:
	api = get_api(ARGS.philips_hue_ip)

	# use groups

	if ARGS.philips_hue_group:
		groups = get_groups(api.get_group(), ARGS.philips_hue_group)

		if not groups:
			exit(wording.get('group_no') + wording.get('exclamation_mark'))
		return process_groups(groups, status)

	# use lights

	lights = get_lights(api.get_light_objects(), ARGS.philips_hue_light)

	if not lights:
		exit(wording.get('light_no') + wording.get('exclamation_mark'))
	return process_lights(lights, status)


def discover_ips() -> List[str]:
	ips = []
	message =\
	[
		'M-SEARCH * HTTP/1.1',
		'MAN: "ssdp:discover"'
	]
	discovery = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	discovery.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
	discovery.settimeout(2)
	discovery.sendto('\r\n'.join(message).encode(), ('239.255.255.250', 1900))

	try:
		ips.append(helper.get_first(discovery.recvfrom(65507)[1]))
	except socket.timeout:
		print(wording.get('ip_no').format('PHILIPS HUE BRIDGE') + wording.get('exclamation_mark'))
	return ips
