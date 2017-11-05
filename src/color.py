color =\
{
	'yellow': '\033[0;33m',
	'green': '\033[0;32m',
	'red': '\033[0;31m',
	'white': '\033[0;37m',
	'end': '\033[0m'
}


def get(key):
	return color[key]


def end():
	return color['end']