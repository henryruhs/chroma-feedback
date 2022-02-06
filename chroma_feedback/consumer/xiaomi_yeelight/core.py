import socket
import sys
from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, logger, wording
from chroma_feedback.typing import Consumer, ProducerReport
from .light import get_lights, process_lights

ARGS = None


def support() -> bool:
	return helper.is_linux() is True or helper.is_mac() is True or helper.is_windows() is True


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		light_ips = None

		if not helper.has_argument('--xiaomi-yeelight-light-ip'):
			light_ips = discover_light_ips()
		if light_ips:
			program.add_argument('--xiaomi-yeelight-light-ip', default = light_ips)
		else:
			program.add_argument('--xiaomi-yeelight-light-ip', action = 'append', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	lights = get_lights(ARGS.xiaomi_yeelight_light_ip)

	if not lights:
		logger.error(wording.get('light_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_lights(lights, producer_report)


def discover_light_ips() -> List[str]:
	light_ips = []
	message =\
	[
		'M-SEARCH * HTTP/1.1',
		'MAN: "ssdp:discover"',
		'ST: wifi_bulb'
	]
	discovery = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	discovery.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
	discovery.settimeout(2)
	discovery.sendto('\r\n'.join(message).encode(), ('239.255.255.250', 1982))

	try:
		light_ips.append(helper.get_first(discovery.recvfrom(65507)[1]))
	except socket.timeout:
		logger.warn(wording.get('ip_not_found').format('light') + wording.get('exclamation_mark'))
	return light_ips
