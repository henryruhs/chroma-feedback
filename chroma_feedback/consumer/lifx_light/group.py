from typing import Any, List
from chroma_feedback import color
from chroma_feedback.typing import StatusType, ConsumerModel, ColorConfigModel
from .api import get_api


def get_groups(group_names : List[str]) -> Any:
	api = get_api()
	groups = []

	if group_names:
		for group_name in group_names:
			groups.append(api.get_devices_by_group(group_name))
	return groups


def get_group_name(group : Any) -> Any:
	for device in group.get_device_list():
		return device.get_group_label()


def process_groups(groups : Any, status : StatusType) -> List[ConsumerModel]:
	result : List[ConsumerModel] = []

	# process groups

	for group in groups:
		result.append(
		{
			'consumer': 'lifx_light',
			'type': 'group',
			'name': get_group_name(group),
			'active': set_group(group, color.get_by_status(status)),
			'status': status
		})
	return result


def set_group(group : Any, color_config : ColorConfigModel) -> bool:
	return group.set_power('on') is None and group.set_color(
	[
		color_config['hue'],
		color_config['saturation'][2],
		color_config['brightness'][2],
		color_config['kelvin']
	]) is None
