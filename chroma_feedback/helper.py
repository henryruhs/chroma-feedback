import ctypes
import os
import platform
import sys
from typing import Any, Dict


def is_root() -> bool:
	try:
		return os.getuid() == 0 #type:ignore
	except AttributeError:
		try:
			return ctypes.windll.shell32.IsUserAnAdmin() == 1 #type:ignore
		except AttributeError:
			return False


def is_linux() -> bool:
	return to_lower_case(platform.system()) == 'linux'


def is_macos() -> bool:
	return to_lower_case(platform.system()) == 'darwin'


def is_windows() -> bool:
	return to_lower_case(platform.system()) == 'windows'


def parse_slug(slug : str) -> Dict[str, str]:
	if slug:
		return dict(zip([ 'workspace', 'project' ], slug.split('/')))
	return {}


def create_description(name : str, selector : str) -> str:
	if name and selector:
		return name + ' [' + selector + ']'
	return name or selector


def to_lower_case(__string__ : Any) -> str:
	return str(__string__).lower()


def has_argument(argument : str) -> bool:
	return any(argv == argument for argv in sys.argv)


def get_first(__list__ : Any) -> Any:
	if isinstance(__list__, list):
		return next(iter(__list__), None)
	return None


def get_last(__list__ : Any) -> Any:
	if isinstance(__list__, list):
		return next(reversed(__list__), None)
	return None


def remove_duplicate(__list__ : Any) -> Any:
	if isinstance(__list__, list):
		return list(dict.fromkeys(__list__))
	return __list__
