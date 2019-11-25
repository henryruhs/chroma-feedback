from typing import Any, Dict, List
import sys
from requests import Response


def get_provider_status(provider_result : List[Dict[str, Any]]) -> str:
	status = 'passed'

	# process provider

	for provider in provider_result:
		if provider['active'] is True:
			if provider['status'] == 'process':
				if status not in ['errored', 'failed']:
					status = 'process'
			if provider['status'] == 'errored':
				if status != 'failed':
					status = 'errored'
			if provider['status'] == 'failed':
				status = 'failed'
	return status


def parse_json(response : Response) -> Any:
	try:
		return response.json()
	except ValueError:
		return None


def has_argument(argument : str) -> bool:
	return any(argument in argv for argv in sys.argv)


def get_first(__list__ : Any) -> Any:
	return next(iter(__list__), None)
