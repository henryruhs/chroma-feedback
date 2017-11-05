color =\
{
	'yellow': '\033[0;33m',
	'green': '\033[0;32m',
	'red': '\033[0;31m',
	'white': '\033[0;37m',
	'end': '\033[0m'
}


def yellow(text):
	return color['yellow'] + text + color['end']


def green(text):
	return color['green'] + text + color['end']


def red(text):
	return color['red'] + text + color['end']


def white(text):
	return color['white'] + text + color['end']
