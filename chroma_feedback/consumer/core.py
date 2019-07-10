import importlib
from chroma_feedback import wording

def process(status, program):
	args = program.parse_known_args()[0]
	result = []

	for consumer in args.consumer:
		try:
			CONSUMER = importlib.import_module('chroma_feedback.consumer.' + consumer)
			CONSUMER.init(program)
			result.extend(CONSUMER.run(status))
		except ImportError:
			exit(wording.get('consumer_no') + wording.get('exclamation_mark'))
	return result
