from typing import Any, Dict

COLOR =\
{
	'red': '\033[0;31m',
	'green': '\033[0;32m',
	'yellow': '\033[0;33m',
	'end': '\033[0m'
}


def format_red(text : str) -> str:
	return COLOR['red'] + text + COLOR['end']


def format_green(text : str) -> str:
	return COLOR['green'] + text + COLOR['end']


def format_yellow(text : str) -> str:
	return COLOR['yellow'] + text + COLOR['end']


def get_passed() -> Dict[str, Any]:
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


def get_process() -> Dict[str, Any]:
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


def get_errored() -> Dict[str, Any]:
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


def get_failed() -> Dict[str, Any]:
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
