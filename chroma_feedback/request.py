from time import sleep
from typing import Any, Dict

import requests
from requests import RequestException, Response

from chroma_feedback import logger, wording


def get(url : str, headers : Dict[str, str] = None) -> Response:
	try:
		return requests.get(url, headers = headers, timeout = 10)
	except RequestException:
		logger.warn(wording.get('retry_request').format('GET', 10))
		sleep(10)
		return get(url, headers)


def post(url : str, data : Any = None, headers : Dict[str, str] = None) -> Response:
	try:
		return requests.post(url, data, headers = headers, timeout = 10)
	except RequestException:
		logger.warn(wording.get('retry_request').format('POST', 10))
		sleep(10)
		return post(url, data, headers)


def parse_json(response: Response) -> Any:
	try:
		return response.json()
	except ValueError:
		return None
