from typing import Any, Dict, List
import sys
import requests
from requests import Response, RequestException


def get_producer_status(producer_result : List[Dict[str, Any]]) -> str:
	status = 'passed'

	# process producer

	for producer in producer_result:
		if producer['active'] is True:
			if producer['status'] == 'process':
				if status not in ['errored', 'failed']:
					status = 'process'
			if producer['status'] == 'errored':
				if status != 'failed':
					status = 'errored'
			if producer['status'] == 'failed':
				status = 'failed'
	return status


def fetch(url : str, headers : Any = None) -> Response or None:
	try:
		return requests.get(url, headers = headers)
	except RequestException:
		return None


def parse_json(response : Response) -> Any:
	try:
		return response.json()
	except ValueError:
		return None


def to_lower_case(__string__ : Any) -> str:
	return str(__string__).lower()


def has_argument(argument : str) -> bool:
	return any(argument in argv for argv in sys.argv)


def get_first(__list__ : Any) -> Any:
	return next(iter(__list__), None)


def get_last(__list__ : Any) -> Any:
	return next(reversed(__list__), None)
