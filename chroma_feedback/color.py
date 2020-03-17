from typing import Any, Dict

COLOR =\
{
	'red': '\033[0;31m',
	'green': '\033[0;32m',
	'yellow': '\033[0;33m',
	'orange': '\033[38:2:255:165:0m',
	'end': '\033[0m'
}


def format_red(text : str) -> str:
	return COLOR['red'] + text + COLOR['end']


def format_green(text : str) -> str:
	return COLOR['green'] + text + COLOR['end']


def format_yellow(text : str) -> str:
	return COLOR['yellow'] + text + COLOR['end']


def format_orange(text : str) -> str:
	return COLOR['orange'] + text + COLOR['end']


def get_passed() -> Dict[str, Any]:
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

def get_warning() -> Dict[str, Any]:
	return\
	{
		'name': 'orange',
		'rgb':
		[
			255,
			127, # This seems very 'yellow' on a Razer Chroma mouse...is 32 better?
			0
		],
		'hue': 5460,
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


def get_errored() -> Dict[str, Any]:
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


def get_failed() -> Dict[str, Any]:
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
