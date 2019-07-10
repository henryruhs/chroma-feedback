import importlib
from chroma_feedback import wording


def process(program):
	args = program.parse_known_args()[0]
	result = []

	for provider in args.provider:
		try:
			PROVIDER = importlib.import_module('chroma_feedback.provider.' + provider)
			PROVIDER.init(program)
			result.extend(PROVIDER.run())
		except ImportError:
			exit(wording.get('provider_no') + wording.get('exclamation_mark'))
	return result
