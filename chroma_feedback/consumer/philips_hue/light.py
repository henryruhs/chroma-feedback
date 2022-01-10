from typing import Any, List
import copy
from chroma_feedback import color, helper
from chroma_feedback.typing import Color, Consumer, Producer, Status
from .api import get_api


def get_lights(lights : Any, light_names : List[str]) -> Any:
	if light_names:
		for light in copy.copy(lights):
			if light.name not in light_names:
				lights.remove(light)
	return lights


def process_lights(lights : Any, producer_result : List[Producer]) -> List[Consumer]:
	result : List[Consumer] = []
	status: Status = helper.resolve_producer_status(producer_result)

	# process lights

	for light in lights:
		result.append(
		{
			'consumer': 'philips_hue',
			'type': 'light',
			'name': light.name,
			'active': set_light(light.name, color.get_by_status(status)),
			'status': status
		})
	return result


def set_light(light_name : str, color_config : Color) -> bool:
	api = get_api(None)

	return api is not None and api.set_light(light_name,
	{
		'hue': color_config['hue'],
		'sat': color_config['saturation'][1],
		'bri': color_config['brightness'][1],
		'on': True,
		'alert': 'none'
	}) is not None
