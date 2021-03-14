from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper
from .device import process_devices

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--luxafor-host', default='https://api.luxafor.com')
		program.add_argument('--luxafor-id', action = 'append', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run(status : str) -> List[Dict[str, Any]]:
	return process_devices(ARGS.luxafor_host, ARGS.luxafor_id, status)
