color =\
{
	'red': '\033[0;31m',
	'green': '\033[0;32m',
	'yellow': '\033[0;33m',
	'end': '\033[0m'
}


def red(text):
	return color['red'] + text + color['end']


def green(text):
	return color['green'] + text + color['end']


def yellow(text):
	return color['yellow'] + text + color['end']
