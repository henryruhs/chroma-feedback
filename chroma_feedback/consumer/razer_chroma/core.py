from chroma_feedback import wording
from .device import get_devices, process_devices
from .api import get_api

ARGS = None


def init(program):
	global ARGS

	if not ARGS:
		program.add_argument('--razer-chroma-device', action = 'append')
	ARGS = program.parse_known_args()[0]


def run(status):
	api = get_api()
	devices = get_devices(api.devices, ARGS.razer_chroma_device)

	if not devices:
		exit(wording.get('device_no') + wording.get('exclamation_mark'))
	return process_devices(status, devices)
