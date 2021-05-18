from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, wording
from chroma_feedback.typing import StatusType
from .api import get_api
from .group import get_groups, process_groups
from .light import get_lights, process_lights

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--lifx-light-light', action = 'append')
		program.add_argument('--lifx-light-group', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(status : StatusType) -> List[Dict[str, Any]]:
	api = get_api()

	# use groups

	if ARGS.lifx_light_group:
		groups = get_groups(ARGS.lifx_light_group)

		if not groups:
			exit(wording.get('group_no') + wording.get('exclamation_mark'))
		return process_groups(groups, status)

	# use lights

	lights = get_lights(api.get_lights(), ARGS.lifx_light_light)

	if not lights:
		exit(wording.get('light_no') + wording.get('exclamation_mark'))
	return process_lights(lights, status)
