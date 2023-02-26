from chroma_feedback import helper
from chroma_feedback.typing import Color, Status

COLOR =\
{
	'red': '\033[0;31m',
	'green': '\033[0;32m',
	'yellow': '\033[0;33m',
	'blue': '\033[0;34m',
	'white': '\033[0;37m',
	'end': '\033[0m'
}


def format_by_status(text : str, status : Status) -> str:
	if status == 'started':
		return format_started(text)
	if status == 'errored':
		return format_errored(text)
	if status == 'warned':
		return format_warned(text)
	if status == 'failed':
		return format_failed(text)
	return format_passed(text)


def format_passed(text : str) -> str:
	if not helper.is_windows():
		return COLOR['green'] + text + COLOR['end']
	return text


def format_started(text : str) -> str:
	if not helper.is_windows():
		return COLOR['blue'] + text + COLOR['end']
	return text


def format_errored(text : str) -> str:
	if not helper.is_windows():
		return COLOR['white'] + text + COLOR['end']
	return text


def format_warned(text : str) -> str:
	if not helper.is_windows():
		return COLOR['yellow'] + text + COLOR['end']
	return text


def format_failed(text : str) -> str:
	if not helper.is_windows():
		return COLOR['red'] + text + COLOR['end']
	return text


def get_by_status(status : Status) -> Color:
	if status == 'started':
		return get_started()
	if status == 'errored':
		return get_errored()
	if status == 'warned':
		return get_warned()
	if status == 'failed':
		return get_failed()
	return get_passed()


def get_passed() -> Color:
	return\
	{
		'rgb':
		[
			0,
			255,
			0
		],
		'hue': 26000,
		'saturation':
		[
			100,
			255,
			65535
		],
		'brightness':
		[
			100,
			255,
			65535
		],
		'kelvin': 3500
	}


def get_started() -> Color:
	return\
	{
		'rgb':
		[
			0,
			0,
			255
		],
		'hue': 46000,
		'saturation':
		[
			100,
			255,
			65535
		],
		'brightness':
		[
			100,
			255,
			65535
		],
		'kelvin': 3500
	}


def get_errored() -> Color:
	return\
	{
		'rgb':
		[
			255,
			255,
			255
		],
		'hue': 58000,
		'saturation':
		[
			0,
			0,
			0
		],
		'brightness':
		[
			100,
			255,
			65535
		],
		'kelvin': 3500
	}


def get_warned() -> Color:
	return\
	{
		'rgb':
		[
			255,
			255,
			0
		],
		'hue': 10000,
		'saturation':
		[
			100,
			255,
			65535
		],
		'brightness':
		[
			100,
			255,
			65535
		],
		'kelvin': 3500
	}


def get_failed() -> Color:
	return\
	{
		'rgb':
		[
			255,
			0,
			0
		],
		'hue': 0,
		'saturation':
		[
			100,
			255,
			65535
		],
		'brightness':
		[
			100,
			255,
			65535
		],
		'kelvin': 3500
	}


def get_reset() -> Color:
	return\
	{
		'rgb':
		[
			0,
			0,
			0
		],
		'hue': 0,
		'saturation':
		[
			0,
			0,
			0
		],
		'brightness':
		[
			0,
			0,
			0
		],
		'kelvin': 0
	}
