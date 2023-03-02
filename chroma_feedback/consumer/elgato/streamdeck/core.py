import sys
from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, logger, wording
from chroma_feedback.typing import Consumer, ProducerReport
from .device import filter_devices, get_devices, process_devices

ARGS = None


def support() -> bool:
	return helper.is_linux() or helper.is_mac() or helper.is_windows()


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--elgato-streamdeck-device-id', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	devices = filter_devices(get_devices(), ARGS.elgato_streamdeck_device_id)

	if not devices:
		logger.error(wording.get('device_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_devices(devices, producer_report)
