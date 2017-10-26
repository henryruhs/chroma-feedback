colorArray =\
{
				'passed': '\033[92m',
				'process': '\033[93m',
				'failed': '\033[91m',
				'end': '\033[0m'
}


def get(key):
	return colorArray[key]
