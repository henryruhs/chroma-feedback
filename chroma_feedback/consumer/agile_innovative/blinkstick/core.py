import sys
from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, logger, wording
from chroma_feedback.typing import Consumer, ProducerReport
from .light import filter_lights, get_lights, process_lights

ARGS = None


def support() -> bool:
	return helper.is_linux() or helper.is_macos() or helper.is_windows()


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--agile-innovative-blinkstick-light-serial', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	lights = filter_lights(get_lights(), ARGS.agile_innovative_blinkstick_light_serial)

	if not lights:
		logger.error(wording.get('light_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_lights(lights, producer_report)
