import socket
from chroma_feedback import helper, wording
from .factory import bulb_factory

args = None


def init(program):
	global args

	if not args:
		ip = None

		if not helper.has_argument('--xiaomi-yeelight-ip'):
			ip = discover_ips()
		if ip:
			program.add_argument('--xiaomi-yeelight-ip', default = ip)
		else:
			program.add_argument('--xiaomi-yeelight-ip', action = 'append', required = True)
	args = program.parse_known_args()[0]


def run(status):
	devices = []

	for ip in args.xiaomi_yeelight_ip:
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
	return device.set_rgb(rgb[0], rgb[1], rgb[2]) == 'ok'


def pulsate(device, rgb):
	return device.set_rgb(rgb[0], rgb[1], rgb[2]) == 'ok'


def discover_ips():
	message =\
	[
		'M-SEARCH * HTTP/1.1',
		'HOST: 239.255.255.250:1982',
		'MAN: \'ssdp:discover\'',
		'ST: wifi_bulb'
	]
	SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	SOCKET.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
	SOCKET.settimeout(1)
	SOCKET.sendto('\r\n'.join(message).encode(), ('239.255.255.250', 1982))
	ips = []

	while True:
		try:
			ip = SOCKET.recvfrom(65507)[1][0]
			if ip not in ips:
				ips.append(ip)
		except socket.timeout:
			break
	return ips
