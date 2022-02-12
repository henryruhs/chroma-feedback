from argparse import ArgumentParser
from typing import Any, List

from chroma_feedback import helper, request
from chroma_feedback.typing import Producer
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--vercel-host', default = 'https://api.vercel.com')
		program.add_argument('--vercel-slug', action = 'append')
		program.add_argument('--vercel-token', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[Producer]:
	result = []

	if ARGS.vercel_slug:
		for slug in ARGS.vercel_slug:
			result.extend(fetch(ARGS.vercel_host, slug, ARGS.vercel_token))
	else:
		result.extend(fetch(ARGS.vercel_host, None, ARGS.vercel_token))
	return result


def fetch(host : str, slug : str, token : str) -> List[Producer]:
	result : List[Producer] = []
	response = None

	if host and slug and token:
		response = request.get(host + '/v1/projects/' + slug, headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Bearer ' + token
		})
	elif host and token:
		response = request.get(host + '/v1/projects', headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Bearer ' + token
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'name' in data and 'latestDeployments' in data:
			deployment = helper.get_first(data['latestDeployments'])

			if 'readyState' in deployment:
				result.append(normalize_data(data['name'], deployment['readyState']))
		else:
			for project in data:
				if 'name' in project and 'latestDeployments' in project:
					deployment = helper.get_first(project['latestDeployments'])

					if 'readyState' in deployment:
						result.append(normalize_data(project['name'], deployment['readyState']))
	return result
