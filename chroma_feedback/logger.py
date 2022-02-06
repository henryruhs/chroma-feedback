import logging
from typing import Any

from chroma_feedback.typing import LogLevel


def init(log_level : LogLevel) -> None:
	logging.basicConfig(format = '')
	logging.getLogger().setLevel(get_log_level()[log_level])


def debug(message : str = '') -> None:
	logging.debug(message)


def info(message : str = '') -> None:
	logging.info(message)


def warn(message : str = '') -> None:
	logging.warning(message)


def error(message : str = '') -> None:
	logging.error(message)


def get_log_level() -> Any:
	return \
	{
		'error': logging.ERROR,
		'warn': logging.WARNING,
		'info': logging.INFO,
		'debug': logging.DEBUG
	}
