import sys
from argparse import ArgumentParser
from typing import List, Optional, cast

from chroma_feedback import helper, logger, ssdp, wording
from chroma_feedback.types import Consumer, ProducerReport
from .light import get_lights, process_lights
from .types import Args

ARGS : Optional[Args] = None


def support() -> bool:
	return helper.is_linux() or helper.is_macos() or helper.is_windows()


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

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	lights = get_lights(ARGS.get('xiaomi_yeelight_light_ip'))

	if not lights:
		logger.error(wording.get('light_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_lights(lights, producer_report)


def discover_light_ips() -> List[str]:
	light_ips = ssdp.discover_ips('239.255.255.250', 1982, 'wifi_bulb')

	if not light_ips:
		logger.warn(wording.get('ip_not_found').format('light') + wording.get('exclamation_mark'))
	return light_ips
