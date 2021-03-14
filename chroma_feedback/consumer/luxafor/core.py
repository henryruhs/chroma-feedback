from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, wording
from .device import get_devices, process_device

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--luxafor-host', default='https://api.luxafor.com')
		program.add_argument('--luxafor-id', action = 'append', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run(status : str) -> List[Dict[str, Any]]:
	devices = get_devices(ARGS.luxafor_host, ARGS.luxafor_id)

	if not devices:
		exit(wording.get('device_no') + wording.get('exclamation_mark'))
	# todo: pass devices here to support multiple devices
	return process_device(ARGS.luxafor_host, ARGS.luxafor_id, status)
