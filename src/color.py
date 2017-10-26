colorArray =\
{
				'passed': '\033[0;32m',
				'process': '\033[0;33m',
				'failed': '\033[0;31m',
				'end': '\033[0m'
}


def get(key):
	return colorArray[key]
