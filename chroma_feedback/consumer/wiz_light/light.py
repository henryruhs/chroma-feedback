from typing import Any, List

from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api, get_builder

LIGHTS = []


def get_lights(light_ips : List[str]) -> Any:
	global LIGHTS

	if not LIGHTS:
		for light_ip in light_ips:
			LIGHTS.append(get_api(light_ip))
	return LIGHTS


def process_lights(lights : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process lights

	for light in lights:
		set_light(light, color.get_by_status(status))
		result.append(
		{
			'name': 'wiz_light',
			'type': 'light',
			'description': get_light_name(light) + ' [' + light.ip + ']',
			'status': status
		})
	return result


def get_light_name(light : Any) -> str:
	return light.loop.run_until_complete(light.get_bulbtype()).name


def set_light(light : Any, color_config : Color) -> None:
	builder = get_builder()
	light.loop.run_until_complete(light.turn_on(builder(rgb = color_config['rgb'])))
