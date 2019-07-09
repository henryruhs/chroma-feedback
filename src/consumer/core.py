import importlib
from src import wording

def process(status, program):
	args = program.parse_known_args()[0]
	result = []

	for consumer in args.consumer:
		try:
			CONSUMER = importlib.import_module('src.consumer.' + consumer)
			CONSUMER.init(program)
			result.extend(CONSUMER.run(status))
		except ImportError:
			exit(wording.get('consumer_no') + wording.get('exclamation_mark'))
	return result
