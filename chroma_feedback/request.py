from typing import Any, Dict
import requests
from requests import Response, RequestException


def get(url : str, headers : Dict[str, str] = None) -> Response:
	try:
		return requests.get(url, headers = headers, timeout = 10)
	except RequestException:
		return get(url, headers)


def post(url : str, data : Any = None, headers : Dict[str, str] = None) -> Response:
	try:
		return requests.post(url, data, headers = headers, timeout = 10)
	except RequestException:
		return post(url, data, headers)


def parse_json(response: Response) -> Any:
	try:
		return response.json()
	except ValueError:
		return None
