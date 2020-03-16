from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, wording
from .light import get_lights, process_lights

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		ip = None

		if not helper.has_argument('--magic-hue-ip'):
			ip = discover_ips()
		if ip:
			program.add_argument('--magic-hue-ip', default = ip)
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

	try:
		ips.append('127.1.1.0')
	except OSError:
		print(wording.get('ip_no').format('MAGIC_HUE') + wording.get('exclamation_mark'))
	return ips
