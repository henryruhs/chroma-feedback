import sys
from typing import List
from argparse import ArgumentParser
from chroma_feedback import helper, logger, wording
from chroma_feedback.typing import Consumer, ProducerReport
from .api import get_api
from .group import get_groups, process_groups
from .light import filter_lights, process_lights

ARGS = None


def support() -> bool:
	return helper.is_linux() is True or helper.is_mac() is True or helper.is_windows() is True


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--lifx-light-light-ip', action = 'append')
		program.add_argument('--lifx-light-group-name', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	api = get_api()

	# use groups

	if ARGS.lifx_light_group_name:
		groups = get_groups(ARGS.lifx_light_group_name)

		if not groups:
			logger.error(wording.get('group_not_found') + wording.get('exclamation_mark'))
			sys.exit()
		return process_groups(groups, producer_report)

	# use lights

	lights = filter_lights(api.get_lights(), ARGS.lifx_light_light_ip)

	if not lights:
		logger.error(wording.get('light_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_lights(lights, producer_report)
