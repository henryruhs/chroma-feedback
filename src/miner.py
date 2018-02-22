import src.provider.appveyor as appveyor
import src.provider.circle as circle
import src.provider.jenkins as jenkins
import src.provider.travis as travis


def mine_data(args):
	data = []
	for provider in args.provider:
		if args.slug:
			for slug in args.slug:
				data.extend(fetch_data(provider, args.host, slug, None))
		if args.token:
			data.extend(fetch_data(provider, args.host, None, args.token))
	return data


def fetch_data(provider, host, slug, token):
	if provider == 'appveyor':
		return appveyor.fetch_data(slug, token)
	if provider == 'circle':
		return circle.fetch_data(slug, token)
	if provider == 'jenkins':
		return jenkins.fetch_data(host, slug)
	if provider == 'travis':
		return travis.fetch_data(slug)
	return []
