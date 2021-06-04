import sys
from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, wording
from chroma_feedback.typing import StatusType
from .device import get_devices, process_devices
from .api import get_api

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--thingm-blink1-device', action = 'append')
	ARGS = helper.get_first(program.parse_known_args())


def run(status : StatusType) -> List[Dict[str, Any]]:
	api = get_api()
	devices = get_devices(api.all_lights(), ARGS.thingm_blink1_device)

	if not devices:
		sys.exit(wording.get('device_no') + wording.get('exclamation_mark'))
	return process_devices(devices, status)
