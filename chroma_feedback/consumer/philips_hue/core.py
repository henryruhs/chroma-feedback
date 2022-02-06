import socket
import sys
from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, logger, wording
from chroma_feedback.typing import Consumer, ProducerReport
from .group import filter_groups, get_groups, process_groups
from .light import filter_lights, get_lights, process_lights

ARGS = None


def support() -> bool:
	return helper.is_linux() is True or helper.is_mac() is True or helper.is_windows() is True


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		bridge_ip = None

		if not helper.has_argument('--philips-hue-bridge-ip'):
			bridge_ip = helper.get_first(discover_bridge_ips())
		if bridge_ip:
			program.add_argument('--philips-hue-bridge-ip', default = bridge_ip)
		else:
			program.add_argument('--philips-hue-bridge-ip', required = True)
		program.add_argument('--philips-hue-group-name', action = 'append')
		program.add_argument('--philips-hue-light-id', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	if ARGS.philips_hue_group_name:
		groups = filter_groups(get_groups(ARGS.philips_hue_bridge_ip), ARGS.philips_hue_group_name)

		if not groups:
			logger.error(wording.get('group_not_found') + wording.get('exclamation_mark'))
			sys.exit()
		return process_groups(groups, producer_report)

	# fallback as needed

	lights = filter_lights(get_lights(ARGS.philips_hue_bridge_ip), ARGS.philips_hue_light_id)

	if not lights:
		logger.error(wording.get('light_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_lights(lights, producer_report)


def discover_bridge_ips() -> List[str]:
	bridge_ips = []
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
		bridge_ips.append(helper.get_first(discovery.recvfrom(65507)[1]))
	except socket.timeout:
		logger.warn(wording.get('ip_not_found').format('bridge') + wording.get('exclamation_mark'))
	return bridge_ips
