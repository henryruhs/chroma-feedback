import sys
from typing import List
from argparse import ArgumentParser
from chroma_feedback import helper, wording
from chroma_feedback.typing import Consumer, Producer
from .api import get_api
from .group import get_groups, process_groups
from .light import get_lights, process_lights

ARGS = None


def support() -> bool:
	return helper.is_linux() is True or helper.is_mac() is True or helper.is_windows() is True


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--lifx-light-light', action = 'append')
		program.add_argument('--lifx-light-group', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(producer_result : List[Producer]) -> List[Consumer]:
	api = get_api()

	# use groups

	if ARGS.lifx_light_group:
		groups = get_groups(ARGS.lifx_light_group)

		if not groups:
			sys.exit(wording.get('group_not_found') + wording.get('exclamation_mark'))
		return process_groups(groups, producer_result)

	# use lights

	lights = get_lights(api.get_lights(), ARGS.lifx_light_light)

	if not lights:
		sys.exit(wording.get('light_not_found') + wording.get('exclamation_mark'))
	return process_lights(lights, producer_result)
