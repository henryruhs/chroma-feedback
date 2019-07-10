from chroma_feedback import wording
from .factory import bulb_factory

args = None


def init(program):
	global args

	if not args:
		program.add_argument('--xiaomi-yeeligh-ip', action = 'append', required = True)
	args = program.parse_known_args()[0]


def run(status):
	devices = []

	for ip in args.xiaomi_yeeligh_ip:
		devices.append(bulb_factory(ip))
	if not devices:
		exit(wording.get('device_no') + wording.get('exclamation_mark'))
	return process(status, devices)


def process(status, devices):
	result = []

	# process devices

	for device in devices:
		device_name = device.get_properties()['name']

		if status == 'passed':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'name': device_name,
				'active': static(device, [0, 255, 0]),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'name': device_name,
				'active': static(device, [255, 255, 0]),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'name': device_name,
				'active': pulsate(device, [255, 255, 255]),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'name': device_name,
				'active': pulsate(device, [255, 0, 0]),
				'status': status
			})
	return result


def static(device, rgb):
	return device.set_rgb(rgb[0], rgb[1], rgb[2])


def pulsate(device, rgb):
	return device.set_rgb(rgb[0], rgb[1], rgb[2])
