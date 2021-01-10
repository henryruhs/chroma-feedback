from typing import Any, Dict, List
from chroma_feedback import color
from .api import get_api


def get_lights(ips : List[str]) -> List[Dict[str, Any]]:
	lights = []

	for ip in ips:
		lights.append(get_api(ip))
	return lights


def process_lights(lights : Any, status : str) -> List[Dict[str, Any]]:
	result = []

	# process lights

	for light in lights:
		if status == 'passed':
			result.append(
			{
				'consumer': 'nanoleaf_light',
				'type': 'light',
				'name': light.get_name(),
				'active': static_light(light, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'nanoleaf_light',
				'type': 'light',
				'name': light.get_name(),
				'active': static_light(light, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'nanoleaf_light',
				'type': 'light',
				'name': light.get_name(),
				'active': pulsate_light(light, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'nanoleaf_light',
				'type': 'light',
				'name': light.get_name(),
				'active': pulsate_light(light, color.get_failed()),
				'status': status
			})
	return result


def static_light(light : Any, color_config : Dict[str, Any]) -> bool:
	return light.set_color(color_config['rgb'])


def pulsate_light(light : Any, color_config : Dict[str, Any]) -> bool:
	position_data = []
	device_ids = []
	info_data = light.get_info()

	if 'panelLayout' in info_data and 'layout' in info_data['panelLayout'] and 'positionData' in info_data['panelLayout']['layout']:
		position_data = info_data['panelLayout']['layout']['positionData']

	# process position data

	for data in position_data:
		device_ids.append(data['panelId'])

	animation_data = str(len(device_ids))

	# process devices ids

	for device_id in device_ids:
		animation_data += ' ' + str(device_id) + ' 2 ' + str(color_config['rgb'][0]) + ' ' + str(color_config['rgb'][1]) + ' ' + str(color_config['rgb'][2]) + ' 0 50 0 0 0 0 50'
	return light.write_effect({
		'command': 'display',
		'animType': 'custom',
		'animData': animation_data,
		'loop': True
	})
