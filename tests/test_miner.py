from src import miner


def test_progress_slug(mocker):
	args = mocker.MagicMock()
	args.host = None
	args.provider = []
	args.provider.append('appveyor')
	args.provider.append('circle')
	args.provider.append('github')
	args.provider.append('gitlab')
	args.provider.append('jenkins')
	args.provider.append('teamcity')
	args.provider.append('travis')
	args.slug = []
	args.slug.append('one')
	args.slug.append('two')
	args.auth = None
	fetch = mocker.spy(miner, 'fetch')
	miner.process(args)
	assert fetch.call_count == 14


def test_progress_auth(mocker):
	args = mocker.MagicMock()
	args.host = None
	args.provider = []
	args.provider.append('appveyor')
	args.provider.append('circle')
	args.provider.append('github')
	args.provider.append('gitlab')
	args.provider.append('jenkins')
	args.provider.append('teamcity')
	args.provider.append('travis')
	args.slug = None
	args.auth = 'test'
	fetch = mocker.spy(miner, 'fetch')
	miner.process(args)
	assert fetch.call_count == 7
