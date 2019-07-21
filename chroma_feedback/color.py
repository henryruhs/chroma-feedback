COLOR =\
{
	'red': '\033[0;31m',
	'green': '\033[0;32m',
	'yellow': '\033[0;33m',
	'end': '\033[0m'
}


def format_red(text):
	return COLOR['red'] + text + COLOR['end']


def format_green(text):
	return COLOR['green'] + text + COLOR['end']


def format_yellow(text):
	return COLOR['yellow'] + text + COLOR['end']


def get_passed():
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


def get_process():
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


def get_errored():
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


def get_failed():
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
