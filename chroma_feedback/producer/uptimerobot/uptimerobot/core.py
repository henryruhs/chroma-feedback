from argparse import ArgumentParser
from typing import List

from chroma_feedback import helper, request
from chroma_feedback.typing import Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--uptimerobot-host', default = 'https://api.uptimerobot.com')
		program.add_argument('--uptimerobot-slug', action = 'append')
		program.add_argument('--uptimerobot-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	if ARGS.uptimerobot_slug:
		for slug in ARGS.uptimerobot_slug:
			result.extend(fetch(ARGS.uptimerobot_host, slug, ARGS.uptimerobot_token))
	else:
		result.extend(fetch(ARGS.uptimerobot_host, None, ARGS.uptimerobot_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result = []
	response = None

	if host and slug and token:
		response = request.post(host + '/v2/getMonitors?api_key=' + token,
		{
			'search': slug
		})
	elif host and token:
		response = request.post(host + '/v2/getMonitors?api_key=' + token)

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'monitors' in data:
			for monitor in data['monitors']:
				if 'friendly_name' in monitor and 'url' in monitor and 'status' in monitor:
					result.append(normalize_data(monitor['friendly_name'], monitor['url'], monitor['status']))
	return result
