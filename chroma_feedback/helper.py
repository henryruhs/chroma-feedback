import os
from typing import Any, Dict, List
import platform
import sys
from chroma_feedback.typing import StatusType, ProducerModel


def get_producer_status(producer_result : List[ProducerModel]) -> StatusType:
	status: StatusType = 'passed'

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
	return any(argument in argv for argv in sys.argv)


def get_first(__list__ : Any) -> Any:
	return next(iter(__list__), None)


def get_last(__list__ : Any) -> Any:
	return next(reversed(__list__), None)
