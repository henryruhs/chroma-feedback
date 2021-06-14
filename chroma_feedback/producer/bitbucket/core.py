from typing import List
from argparse import ArgumentParser
import base64
from chroma_feedback import helper, request
from chroma_feedback.typing import ProducerModel
from .normalize import normalize_data

ARGS = None


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		program.add_argument('--bitbucket-host', default = 'https://api.bitbucket.org')
		program.add_argument('--bitbucket-slug', action = 'append')
		program.add_argument('--bitbucket-username', required = True)
		program.add_argument('--bitbucket-password', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run() -> List[ProducerModel]:
	result = []

	for slug in ARGS.bitbucket_slug:
		result.extend(fetch(ARGS.bitbucket_host, slug, ARGS.bitbucket_username, ARGS.bitbucket_password))
	return result


def fetch(host : str, slug : str, username : str, password : str) -> List[ProducerModel]:
	result = []
	response = None

	if host and slug and username and password:
		username_password = username + ':' + password
		response = request.get(host + '/2.0/repositories/' + slug + '/pipelines/', headers =
		{
			'Accept': 'application/json',
			'Authorization': 'Basic ' + base64.b64encode(username_password.encode('utf-8')).decode('ascii')
		})

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'values' in data:
			build = helper.get_first(data['values'])

			if build and 'repository' in build and 'full_name' in build['repository'] and 'state' in build and 'result' in build['state'] and 'name' in build['state']['result']:
				result.append(normalize_data(build['repository']['full_name'], build['state']['result']['name']))
	return result
