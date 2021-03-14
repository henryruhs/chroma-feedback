from typing import Any, Dict, List
from chroma_feedback import color, request


def process_devices(host : str, ids : List[str], status : str) -> List[Dict[str, Any]]:
	result = []

	# process ids

	for id in ids:
		if status == 'passed':
			result.append(
			{
				'consumer': 'luxafor',
				'type': 'device',
				'name': id,
				'active': static_light(host, id, color.get_passed()),
				'status': status
			})
		if status == 'started':
			result.append(
			{
				'consumer': 'luxafor',
				'type': 'device',
				'name': id,
				'active': static_light(host, id, color.get_started()),
				'status': status
			})
		if status == 'errored':
			result.append(
			{
				'consumer': 'luxafor',
				'type': 'device',
				'name': id,
				'active': static_light(host, id, color.get_errored()),
				'status': status
			})
		if status == 'failed':
			result.append(
			{
				'consumer': 'luxafor',
				'type': 'device',
				'name': id,
				'active': static_light(host, id, color.get_failed()),
				'status': status
			})
	return result


def static_light(host : str, id : str, color_config : Dict[str, Any]) -> bool:
	response = None

	if host and id:
		response = request.post(host + '/webhook/v1/actions/solid_color',
		data =
		{
			'userId': id,
			'actionFields':
			{
				'color': color_config['name']
			}
		},
		headers =
		{
			'Content-Type': 'application/json'
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)
		if 'id' in data and id in data['id']:
			return True
	return False
