import requests
from src.provider import appveyor, circle, gitlab, jenkins, travis


def process(args):
	data = []
	for provider in args.provider:
		if args.slug:
			for slug in args.slug:
				data.extend(fetch(provider, args.host, slug, args.token))
		if args.token:
			data.extend(fetch(provider, args.host, None, args.token))
	return data


def fetch(provider, host, slug, token):
	try:
		if provider == 'appveyor':
			return appveyor.fetch(host, slug, token)
		if provider == 'circle':
			return circle.fetch(host, slug, token)
		if provider == 'gitlab':
			return gitlab.fetch(host, slug, token)
		if provider == 'jenkins':
			return jenkins.fetch(host, slug)
		if provider == 'travis':
			return travis.fetch(host, slug)
	except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema):
		pass
	return []
