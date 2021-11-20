import os
from typing import Any, Dict, List
import platform
import sys
from chroma_feedback.typing import Status, Producer


def resolve_producer_status(producer_result : List[Producer]) -> Status:
	status: Status = 'passed'

	# process producer

	for producer in producer_result:
		if producer['active'] is True:
			if producer['status'] == 'started' and status not in ['errored', 'warned' ,'failed']:
				status = 'started'
			if producer['status'] == 'errored' and status not in ['warned' ,'failed']:
				status = 'errored'
			if producer['status'] == 'warned' and status != 'failed':
				status = 'warned'
			if producer['status'] == 'failed':
				status = 'failed'
	return status


def parse_slug(slug : str) -> Dict[str, Any]:
	if slug:
		return dict(zip(['workspace', 'project'], slug.split('/')))
	return {}


def is_root() -> bool:
	return os.geteuid() == 0


def is_linux() -> bool:
	return to_lower_case(platform.system()) == 'linux'


def is_mac() -> bool:
	return to_lower_case(platform.system()) == 'darwin'


def is_windows() -> bool:
	return to_lower_case(platform.system()) == 'windows'


def to_lower_case(__string__ : Any) -> str:
	return str(__string__).lower()


def has_argument(argument : str) -> bool:
	return any(argv.startswith(argument) for argv in sys.argv)


def get_first(__list__ : Any) -> Any:
	return next(iter(__list__), None)


def get_last(__list__ : Any) -> Any:
	return next(reversed(__list__), None)
