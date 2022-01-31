from typing import Any, List

from chroma_feedback import color, reporter
from chroma_feedback.typing import Color, Consumer, ProducerReport, Status
from .api import get_api


def get_lights(ips : List[str]) -> Any:
	lights = []

	for ip in ips:
		lights.append(get_api(ip))
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
				'description': light.get_name(),
				'status': status
			})
	return result


def set_light(light : Any, color_config : Color) -> bool:
	return light.set_color(color_config['rgb'])
