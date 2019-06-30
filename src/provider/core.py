import importlib
import requests


def process(args):
	result = []
	for provider in args.provider:
		if args.slug:
			for slug in args.slug:
				result.extend(fetch(provider, args.host, slug, args.auth))
		elif args.auth:
			result.extend(fetch(provider, args.host, None, args.auth))
	return result


def fetch(provider, host, slug, auth):
	try:
		PROVIDER = importlib.import_module('src.provider.' + provider)
		return PROVIDER.fetch(host, slug, auth)
	except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema):
		pass
	return []
