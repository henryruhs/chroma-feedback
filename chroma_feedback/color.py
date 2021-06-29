from chroma_feedback import helper
from chroma_feedback.typing import StatusType, ColorConfigModel

COLOR =\
{
	'red': '\033[0;31m',
	'green': '\033[0;32m',
	'yellow': '\033[0;33m',
	'end': '\033[0m'
}


def format_passed(text : str) -> str:
	if helper.is_windows() is False:
		return COLOR['green'] + text + COLOR['end']
	return text


def format_started(text : str) -> str:
	if helper.is_windows() is False:
		return COLOR['yellow'] + text + COLOR['end']
	return text


def format_failed(text : str) -> str:
	if helper.is_windows() is False:
		return COLOR['red'] + text + COLOR['end']
	return text


def get_by_status(status : StatusType) -> ColorConfigModel:
	if status == 'started':
		return get_started()
	if status == 'errored':
		return get_errored()
	if status == 'failed':
		return get_failed()
	return get_passed()


def get_passed() -> ColorConfigModel:
	return\
	{
		'name': 'green',
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


def get_started() -> ColorConfigModel:
	return\
	{
		'name': 'yellow',
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


def get_errored() -> ColorConfigModel:
	return\
	{
		'name': 'white',
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


def get_failed() -> ColorConfigModel:
	return\
	{
		'name': 'red',
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
