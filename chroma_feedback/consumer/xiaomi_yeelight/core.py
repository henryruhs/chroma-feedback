import socket
from chroma_feedback import color, helper, wording
from .factory import api_factory

args = None


def init(program):
	global args

	if not args:
		ip = None

		if not helper.has_argument('--xiaomi-yeelight-ip'):
			ip = discover_light_ips()
		if ip:
			program.add_argument('--xiaomi-yeelight-ip', default = ip)
		else:
			program.add_argument('--xiaomi-yeelight-ip', action = 'append', required = True)
	args = program.parse_known_args()[0]


def run(status):
	lights = get_lights(args.xiaomi_yeelight_ip)

	if not lights:
		exit(wording.get('light_no') + wording.get('exclamation_mark'))
	return process(status, lights)


def get_lights(ips):
	lights = []

	for ip in ips:
		lights.append(api_factory(ip))
	return lights


def process(status, lights):
	result = []

	# process lights

	for light in lights:
		light_name = light.get_properties()['name']

		if status == 'passed':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'name': light_name,
				'active': static(light, color.get_passed_rgb()),
				'status': status
			})
		if status == 'process':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'name': light_name,
				'active': static(light, color.get_process_rgb()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'name': light_name,
				'active': static(light, color.get_errored_rgb()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'xiaomi_yeelight',
				'name': light_name,
				'active': static(light, color.get_failed_rgb()),
				'status': status
			})
	return result


def static(light, state):
	return light.set_rgb(state['red'], state['green'], state['blue']) == 'ok'


def discover_light_ips():
	message =\
	[
		'M-SEARCH * HTTP/1.1',
		'HOST: 239.255.255.250:1982',
		'MAN: "ssdp:discover"',
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
