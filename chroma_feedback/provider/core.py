import importlib
from chroma_feedback import wording


def process(program):
	args = program.parse_known_args()[0]
	result = []

	for provider_name in args.provider:
		try:
			provider = importlib.import_module('chroma_feedback.provider.' + provider_name)
			provider.init(program)
			result.extend(provider.run())
		except ImportError:
			exit(wording.get('provider_no') + wording.get('exclamation_mark'))
	return result
