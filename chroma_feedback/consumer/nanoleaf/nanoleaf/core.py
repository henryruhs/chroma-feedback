import sys
from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, logger, ssdp, wording
from chroma_feedback.typing import Consumer, ProducerReport
from .light import get_lights, process_lights

ARGS = None


def support() -> bool:
	return helper.is_linux() or helper.is_mac() or helper.is_windows()


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		light_ips = None

		if not helper.has_argument('--nanoleaf-light-ip'):
			light_ips = discover_light_ips()
		if light_ips:
			program.add_argument('--nanoleaf-light-ip', default = light_ips)
		else:
			program.add_argument('--nanoleaf-light-ip', action = 'append', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	lights = get_lights(ARGS.nanoleaf_light_ip)

	if not lights:
		logger.error(wording.get('light_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_lights(lights, producer_report)


def discover_light_ips() -> List[str]:
	light_ips = ssdp.discover_ips('239.255.255.250', 1900, 'nanoleaf:nl29')

	if light_ips is None:
		logger.warn(wording.get('ip_not_found').format('light') + wording.get('exclamation_mark'))
	return light_ips
