from typing import Any, Dict, List
from chroma_feedback import color
from chroma_feedback.typing import StatusType
from .api import get_api


def get_lights(ips : List[str]) -> List[Dict[str, Any]]:
	lights = []

	for ip in ips:
		lights.append(get_api(ip))
	return lights


def process_lights(lights : Any, status : StatusType) -> List[Dict[str, Any]]:
	result = []

	# process lights

	for light in lights:
		result.append(
		{
			'consumer': 'xiaomi_yeelight',
			'type': 'light',
			'name': light.get_properties()['name'],
			'active': set_light(light, color.get_by_status(status)),
			'status': status
		})
	return result


def set_light(light : Any, color_config : Dict[str, Any]) -> bool:
	return light.turn_on() == 'ok' and light.set_rgb(color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2]) == 'ok'
