import os
from typing import Any
from chroma_feedback import request, wording

API = None


def get_api(ip : str) -> Any:
	global API

	if not API:
		API = api_factory(ip)
	return API


def get_token(ip : str) -> Any:
	file_path = os.path.expanduser('~') + '/.nanoleaf_token'

	if os.path.exists(file_path) is False:
		open(file_path, 'w')
	token = open(file_path, 'r').read()
	if token:
		return token

	response = request.post('http://' + ip + ':16021/api/v1/new')

	# process response

	if response and response.status_code == 200:
		data = request.parse_json(response)

		if 'auth_token' in data:
			open(file_path, 'w').write(data['auth_token'])
			return data['auth_token']
	return None


def api_factory(ip : str) -> Any:
	api = None
	token = get_token(ip)

	try:
		from nanoleafapi import Nanoleaf

		try:
			api = Nanoleaf(ip, token)
		except:
			exit(wording.get('connection_no').format('NANOLEAF LIGHT') + wording.get('exclamation_mark'))
		if token is None:
			exit(wording.get('press_button').format('PAIRING', 'NANOLEAF LIGHT') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		exit(wording.get('package_no').format('NANOLEAF LIGHT') + wording.get('exclamation_mark'))
