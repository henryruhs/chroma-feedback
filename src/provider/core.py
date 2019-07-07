import importlib


def process(program):
	args = program.parse_known_args()[0]
	result = []

	for provider in args.provider:
		try:
			PROVIDER = importlib.import_module('src.provider.' + provider)
			PROVIDER.init(program)
			result.extend(PROVIDER.run())
		except ModuleNotFoundError:
			pass
	return result
