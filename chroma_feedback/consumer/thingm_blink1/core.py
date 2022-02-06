import sys
from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, logger, wording
from chroma_feedback.typing import Consumer, ProducerReport
from .lights import filter_lights, get_lights, process_lights

ARGS = None


def support() -> bool:
	return helper.is_linux() is True or helper.is_mac() is True


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--thingm-blink1-light-serial', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	lights = filter_lights(get_lights(), ARGS.thingm_blink1_light_serial)

	if not lights:
		logger.error(wording.get('light_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_lights(lights, producer_report)
