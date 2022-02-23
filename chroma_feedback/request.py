import base64
from time import sleep
from typing import Any

import requests
from requests import RequestException, Response

from chroma_feedback import logger, wording
from chroma_feedback.typing import Headers


def get(url : str, headers : Headers = None) -> Response:
	try:
		response = requests.get(url, headers = headers, timeout = 10)
		logger.debug(wording.get('fetch_request').format('GET', response.url, response.status_code))
		return response
	except RequestException:
		logger.warn(wording.get('retry_request').format('GET', 10))
		sleep(10)
		return get(url, headers)


def post(url : str, data : Any = None, headers : Headers = None) -> Response:
	try:
		response = requests.post(url, data, headers = headers, timeout = 10)
		logger.debug(wording.get('fetch_request').format('POST', response.url, response.status_code))
		return response
	except RequestException:
		logger.warn(wording.get('retry_request').format('POST', 10))
		sleep(10)
		return post(url, data, headers)


def parse_json(response: Response) -> Any:
	try:
		return response.json()
	except ValueError:
		return None


def create_basic_auth_headers(username : str, password : str) -> Headers:
	username_password = username + ':' + password

	return\
	{
		'Accept': 'application/json',
		'Authorization': 'Basic ' + base64.b64encode(username_password.encode('utf-8')).decode('ascii')
	}


def create_bearer_auth_headers(token : str) -> Headers:
	return\
	{
		'Accept': 'application/json',
		'Authorization': 'Bearer ' + token
	}
