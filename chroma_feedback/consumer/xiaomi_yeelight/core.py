from typing import Any, Dict, List
from argparse import ArgumentParser
import socket
from chroma_feedback import helper, wording
from .light import get_lights, process_lights

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		ips = None

		if not helper.has_argument('--xiaomi-yeelight-ip'):
			ips = discover_ips()
		if ips:
			program.add_argument('--xiaomi-yeelight-ip', default = ips)
		else:
			program.add_argument('--xiaomi-yeelight-ip', action = 'append', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run(status : str) -> List[Dict[str, Any]]:
	lights = get_lights(ARGS.xiaomi_yeelight_ip)

	if not lights:
		exit(wording.get('light_no') + wording.get('exclamation_mark'))
	return process_lights(lights, status)


def discover_ips() -> List[str]:
	ips = []
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
		ips.append(helper.get_first(discovery.recvfrom(65507)[1]))
	except socket.timeout:
		print(wording.get('ip_no').format('XIAOMI YEELIGHT') + wording.get('exclamation_mark'))
	return ips
