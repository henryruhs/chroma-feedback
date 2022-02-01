import sys
from typing import List
from argparse import ArgumentParser
import socket
from chroma_feedback import helper, logger, wording
from chroma_feedback.typing import Consumer, ProducerReport
from .group import get_groups, process_groups
from .light import get_lights, process_lights
from .api import get_api

ARGS = None


def support() -> bool:
	return helper.is_linux() is True or helper.is_mac() is True or helper.is_windows() is True


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


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	api = get_api(ARGS.philips_hue_ip)

	# use groups

	if ARGS.philips_hue_group:
		groups = get_groups(api.get_group(), ARGS.philips_hue_group)

		if not groups:
			logger.error(wording.get('group_not_found') + wording.get('exclamation_mark'))
			sys.exit()
		return process_groups(groups, producer_report)

	# use lights

	lights = get_lights(api.get_light_objects(), ARGS.philips_hue_light)

	if not lights:
		logger.error(wording.get('light_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_lights(lights, producer_report)


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
		logger.error(wording.get('ip_not_found').format('PHILIPS HUE BRIDGE') + wording.get('exclamation_mark'))
		sys.exit()
	return ips
