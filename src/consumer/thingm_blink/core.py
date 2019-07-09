args = None


def init(program):
	global args

	args = program.parse_known_args()[0]


def run(status):
	devices = []

	return process(status, devices)


def process(status, devices):
	result = []

	return result
