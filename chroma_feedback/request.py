from typing import Any
import requests
from requests import Response, RequestException


def get(url : str, headers : Any = None) -> Any:
	try:
		return requests.get(url, headers = headers)
	except RequestException:
		return None


def post(url : str, headers : Any = None) -> Any:
	try:
		return requests.post(url, headers = headers)
	except RequestException:
		return None


def parse_json(response: Response) -> Any:
	try:
		return response.json()
	except ValueError:
		return None
