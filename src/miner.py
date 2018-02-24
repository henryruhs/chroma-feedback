from src.provider import appveyor, circle, jenkins, travis


def process(args):
	data = []
	for provider in args.provider:
		if args.slug:
			for slug in args.slug:
				data.extend(fetch(provider, args.host, slug, None))
		if args.token:
			data.extend(fetch(provider, args.host, None, args.token))
	return data


def fetch(provider, host, slug, token):
	if provider == 'appveyor':
		return appveyor.fetch(slug, token)
	if provider == 'circle':
		return circle.fetch(slug, token)
	if provider == 'jenkins':
		return jenkins.fetch(host, slug)
	if provider == 'travis':
		return travis.fetch(slug)
	return []
