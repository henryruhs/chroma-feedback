import importlib


def process(status, program):
	args = program.parse_known_args()[0]
	result = []

	for consumer in args.consumer:
		try:
			CONSUMER = importlib.import_module('src.consumer.' + consumer)
			CONSUMER.init(program)
			result.append(CONSUMER.run(status))
		except ImportError:
			pass
	return result
