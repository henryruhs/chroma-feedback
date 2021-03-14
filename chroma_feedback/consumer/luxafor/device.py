import json

from typing import Any, Dict, List
from chroma_feedback import request
from chroma_feedback import color

def process_device(webhook_id : str, status : str) -> List[Dict[str, Any]]:
	result = []

	if status == 'passed':
		result.append(
		{
			'consumer': 'luxafor',
			'type': 'device',
			'name': webhook_id,
			'active': static_light(webhook_id, color.get_passed()),
			'status': status
		})
	if status == 'started':
		result.append(
		{
			'consumer': 'luxafor',
			'type': 'device',
			'name': webhook_id,
			'active': static_light(webhook_id, color.get_started()),
			'status': status
		})
	if status == 'errored':
		result.append(
		{
			'consumer': 'luxafor',
			'type': 'device',
			'name': webhook_id,
			'active': static_light(webhook_id, color.get_errored()),
			'status': status
		})
	if status == 'failed':
		result.append(
		{
			'consumer': 'luxafor',
			'type': 'device',
			'name': webhook_id,
			'active': static_light(webhook_id, color.get_failed()),
			'status': status
		})
	return result


def static_light(webhook_id : str, color_config : Dict[str, Any]) -> bool:
	hexa_color = get_color(color_config)
	body = {
			"userId": webhook_id,
			"actionFields": {
				"color": "custom",
				"custom_color": hexa_color
			}
		}

	response = request.post('https://api.luxafor.com/webhook/v1/actions/solid_color', headers =
	{
		'Content-Type': 'application/json'
	}, data = json.dumps(body))
	return response and response.status_code == 200


def get_color(color_config : Dict[str, Any]) -> str:
	return '%02x%02x%02x' % (color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2])
