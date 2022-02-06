from typing import Any, List

from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api, get_builder, get_loop


def get_lights(light_ips : List[str]) -> Any:
	lights = []

	for light_ip in light_ips:
		lights.append(get_api(light_ip))
	return lights


def process_lights(lights : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process lights

	for light in lights:
		if set_light(light, color.get_by_status(status)):
			result.append(
			{
				'name': 'wiz_light',
				'type': 'light',
				'description': get_light_name(light),
				'status': status
			})
	return result


def get_light_name(light : Any) -> str:
	loop = get_loop()
	config = loop.run_until_complete(light.get_bulbtype())
	return config.name


def set_light(light : Any, color_config : Color) -> bool:
	loop = get_loop()
	builder = get_builder()
	loop.run_until_complete(light.turn_on(builder(rgb = color_config['rgb'])))
	return loop.is_closed() is False
