from logging import basicConfig, getLogger, Logger, DEBUG, INFO, WARNING, ERROR
from typing import Any

from chroma_feedback.typing import LogLevel


def init(log_level : LogLevel) -> None:
	basicConfig(format = '')
	get_package_logger().setLevel(get_log_level()[log_level])


def get_package_logger() -> Logger:
	return getLogger('chroma_feedback')


def debug(message : str = '') -> None:
	get_package_logger().debug(message)


def info(message : str = '') -> None:
	get_package_logger().info(message)


def warn(message : str = '') -> None:
	get_package_logger().warning(message)


def error(message : str = '') -> None:
	get_package_logger().error(message)


def get_log_level() -> Any:
	return\
	{
		'error': ERROR,
		'warn': WARNING,
		'info': INFO,
		'debug': DEBUG
	}
