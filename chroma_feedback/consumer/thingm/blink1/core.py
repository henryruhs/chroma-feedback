import sys
from argparse import ArgumentParser
from typing import List, Optional, cast

from chroma_feedback import helper, logger, wording
from chroma_feedback.types import Consumer, ProducerReport
from .light import filter_lights, get_lights, process_lights
from .types import Args

ARGS : Optional[Args] = None


def support() -> bool:
	return helper.is_linux() or helper.is_macos() or helper.is_windows()


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--thingm-blink1-light-serial', action = 'append')

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	lights = filter_lights(get_lights(), ARGS.get('thingm_blink1_light_serial'))

	if not lights:
		logger.error(wording.get('light_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_lights(lights, producer_report)
