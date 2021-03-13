from typing import Any, Dict, List
from argparse import ArgumentParser
from chroma_feedback import helper, wording
from .device import process_device

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--luxafor-webhook-id', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run(status : str) -> List[Dict[str, Any]]:
	webhook_id = ARGS.luxafor_webhook_id

	if not webhook_id:
		exit(wording.get('device_no') + wording.get('exclamation_mark'))
	return process_device(webhook_id, status)
