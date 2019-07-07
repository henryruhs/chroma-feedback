import importlib
import requests


def process(program):
	args = program.parse_known_args()[0]
	result = []

	for provider in args.provider:
		result.extend(load(provider, program))
	return result


def load(provider, program):
	try:
		PROVIDER = importlib.import_module('src.provider.' + provider)
		PROVIDER.init(program)
		return PROVIDER.run()
	except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema):
		pass
	return []
