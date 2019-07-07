import importlib


def process(reporter_result, program):
	args = program.parse_known_args()[0]
	result = []

	for consumer in args.consumer:
		try:
			CONSUMER = importlib.import_module('src.consumer.' + consumer)
			CONSUMER.init(program)
			result.append(CONSUMER.run(reporter_result['status']))
		except ImportError:
			pass
	return result
