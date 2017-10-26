colorArray =\
{
				'process': '\033[0;33m',
				'passed': '\033[0;32m',
				'failed': '\033[0;31m',
				'end': '\033[0m'
}


def get(key):
	return colorArray[key]
