COLOR =\
{
	'red': '\033[0;31m',
	'green': '\033[0;32m',
	'yellow': '\033[0;33m',
	'end': '\033[0m'
}


def red(text):
	return COLOR['red'] + text + COLOR['end']


def green(text):
	return COLOR['green'] + text + COLOR['end']


def yellow(text):
	return COLOR['yellow'] + text + COLOR['end']


def get_passed_rgb():
	return\
	{
		'red': 0,
		'green': 255,
		'blue': 0
	}


def get_process_rgb():
	return\
	{
		'red': 255,
		'green': 255,
		'blue': 0
	}


def get_errored_rgb():
	return\
	{
		'red': 255,
		'green': 255,
		'blue': 255
	}


def get_failed_rgb():
	return\
	{
		'red': 255,
		'green': 0,
		'blue': 0
	}


def get_passed_hue():
	return\
	{
		'hue': 26000,
		'saturation': 255
	}


def get_process_hue():
	return\
	{
		'hue': 10000,
		'saturation': 255
	}


def get_errored_hue():
	return\
	{
		'hue': 10000,
		'saturation': 0
	}


def get_failed_hue():
	return\
	{
		'hue': 0,
		'saturation': 255
	}
