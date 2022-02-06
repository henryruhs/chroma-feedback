from typing import Any, List

from chroma_feedback import color, helper, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api


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
				'name': 'nanoleaf_light',
				'type': 'light',
				'description': helper.create_description(light.get_name(), light.ip),
				'status': status
			})
	return result


def set_light(light : Any, color_config : Color) -> bool:
	return light.set_color(color_config['rgb'])
