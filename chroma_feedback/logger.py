from logging import DEBUG, ERROR, INFO, Logger, WARNING, basicConfig, getLogger
from typing import Dict

from chroma_feedback.types import LogLevel


def init(log_level : LogLevel) -> None:
	basicConfig(format = '%(message)s')
	get_package_logger().setLevel(get_log_levels()[log_level])


def get_package_logger() -> Logger:
	return getLogger('chroma_feedback')


def debug(message : str) -> None:
	get_package_logger().debug(message)


def info(message : str) -> None:
	get_package_logger().info(message)


def warn(message : str) -> None:
	get_package_logger().warning(message)


def error(message : str) -> None:
	get_package_logger().error(message)


def get_log_levels() -> Dict[LogLevel, int]:
	return\
	{
		'error': ERROR,
		'warn': WARNING,
		'info': INFO,
		'debug': DEBUG
	}
