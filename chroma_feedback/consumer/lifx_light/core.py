import sys
from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, logger, wording
from chroma_feedback.typing import Consumer, ProducerReport
from .group import get_groups, process_groups
from .light import filter_lights, get_lights, process_lights

ARGS = None


def support() -> bool:
	return helper.is_linux() is True or helper.is_mac() is True or helper.is_windows() is True


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--lifx-light-group-name', action = 'append')
		program.add_argument('--lifx-light-light-ip', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	if ARGS.lifx_light_group_name:
		groups = get_groups(ARGS.lifx_light_group_name)

		if not groups:
			logger.error(wording.get('group_not_found') + wording.get('exclamation_mark'))
			sys.exit()
		return process_groups(groups, producer_report)

	# fallback as needed

	lights = filter_lights(get_lights(), ARGS.lifx_light_light_ip)

	if not lights:
		logger.error(wording.get('light_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_lights(lights, producer_report)
