import sys
from typing import List
from argparse import ArgumentParser
from chroma_feedback import helper, logger, wording
from chroma_feedback.typing import Consumer, ProducerReport
from .device import get_devices, process_devices
from .api import get_api

ARGS = None


def support() -> bool:
	return helper.is_linux() is True or helper.is_mac() is True


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--thingm-blink1-device', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(producer_report : List[ProducerReport]) -> List[Consumer]:
	api = get_api()
	devices = get_devices(api.all_lights(), ARGS.thingm_blink1_device)

	if not devices:
		logger.error(wording.get('device_not_found') + wording.get('exclamation_mark'))
		sys.exit()
	return process_devices(devices, producer_report)
