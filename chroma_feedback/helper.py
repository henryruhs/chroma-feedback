from typing import Any, Dict, List
import platform
import sys


def get_producer_status(producer_result : List[Dict[str, Any]]) -> str:
	status = 'passed'

	# process producer

	for producer in producer_result:
		if producer['active'] is True:
			if producer['status'] == 'started':
				if status not in ['errored', 'failed']:
					status = 'started'
			if producer['status'] == 'errored':
				if status != 'failed':
					status = 'errored'
			if producer['status'] == 'failed':
				status = 'failed'
	return status


def to_lower_case(__string__ : Any) -> str:
	return str(__string__).lower()


def has_argument(argument : str) -> bool:
	return any(argument in argv for argv in sys.argv)


def is_linux() -> bool:
	return to_lower_case(platform.system()) == 'linux'


def get_first(__list__ : Any) -> Any:
	return next(iter(__list__), None)


def get_last(__list__ : Any) -> Any:
	return next(reversed(__list__), None)
