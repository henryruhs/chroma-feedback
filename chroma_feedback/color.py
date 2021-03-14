from typing import Any, Dict

COLOR =\
{
	'failed': '\033[0;31m',
	'passed': '\033[0;32m',
	'started': '\033[0;33m',
	'end': '\033[0m'
}


def format_passed(text : str) -> str:
	return COLOR['passed'] + text + COLOR['end']


def format_started(text : str) -> str:
	return COLOR['started'] + text + COLOR['end']


def format_failed(text : str) -> str:
	return COLOR['failed'] + text + COLOR['end']


def get_by_status(status : str) -> Dict[str, Any]:
	if status == 'started':
		return get_started()
	if status == 'errored':
		return get_errored()
	if status == 'failed':
		return get_failed()
	return get_passed()


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


def get_started() -> Dict[str, Any]:
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
