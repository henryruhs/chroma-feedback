import sys
from argparse import ArgumentParser
from typing import List, Optional, cast

from chroma_feedback import helper, logger, wording
from chroma_feedback.types import Consumer, ProducerReport
from .device import filter_devices, get_devices, process_devices
from .types import Args

ARGS : Optional[Args] = None


def support() -> bool:
	return helper.is_linux()


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--razer-chroma-device-serial', action = 'append')

	args, _ = program.parse_known_args()
	ARGS = cast(Args, vars(args))


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	devices = filter_devices(get_devices(), ARGS.get('razer_chroma_device_serial'))

	if not devices:
		logger.error(wording.get('device_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_devices(devices, producer_report)
