from src import provider


def test_progress_slug(mocker):
	args = mocker.MagicMock()
	args.host = None
	args.provider =\
	[
		'appveyor',
		'circle',
		'github',
		'gitlab',
		'jenkins',
		'teamcity',
		'travis'
	]
	args.slug =\
	[
		'one',
		'two'
	]
	args.auth = None
	fetch = mocker.spy(provider.core, 'fetch')
	provider.process(args)
	assert fetch.call_count == len(args.provider) * 2


def test_progress_auth(mocker):
	args = mocker.MagicMock()
	args.host = None
	args.provider =\
	[
		'appveyor',
		'circle',
		'github',
		'gitlab',
		'jenkins',
		'teamcity',
		'travis'
	]
	args.slug = None
	args.auth = 'test'
	fetch = mocker.spy(provider.core, 'fetch')
	provider.process(args)
	assert fetch.call_count == len(args.provider)
