import sys
from typing import List
from argparse import ArgumentParser
from chroma_feedback import helper, wording
from chroma_feedback.typing import Consumer, Producer
from .device import get_devices, process_devices
from .api import get_api

ARGS = None


def support() -> bool:
	return helper.is_linux() is True or helper.is_mac() is True or helper.is_windows() is True


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--elgato-streamdeck-device', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(producer_result : List[Producer]) -> List[Consumer]:
	api = get_api()
	devices = get_devices(api.enumerate(), ARGS.elgato_streamdeck_device)

	if not devices:
		sys.exit(wording.get('device_not_found') + wording.get('exclamation_mark'))
	return process_devices(devices, producer_result)