import socket
from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, wording
from .light import get_lights, process_lights

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		ips = None

		if not helper.has_argument('--magic-hue-ip'):
			ips = discover_ips()
		if ips:
			program.add_argument('--magic-hue-ip', default = ips)
		else:
			program.add_argument('--magic-hue-ip', action = 'append', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run(status : str) -> List[Dict[str, Any]]:
	lights = get_lights(ARGS.magic_hue_ip)

	if not lights:
		exit(wording.get('light_no') + wording.get('exclamation_mark'))
	return process_lights(lights, status)


def discover_ips() -> List[str]:
	ips = []
	message =\
	[
		'HF-A11ASSISTHREAD'
	]
	discovery = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	discovery.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	discovery.settimeout(2)
	discovery.sendto('\r\n'.join(message).encode(), ('255.255.255.255', 48899))

	try:
		ips.append(helper.get_first(discovery.recvfrom(65507)[1]))
	except OSError:
		print(wording.get('ip_no').format('MAGIC HUE') + wording.get('exclamation_mark'))
	return ips
