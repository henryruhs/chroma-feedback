from src import reporter


def test_process_passed():
	data = reporter.process(data =
	[
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	])
	assert 'Build of redaxmedia/chroma-feedback on travis passed' in data['message'][0]
	assert data['status'] == 'passed'


def test_process_process():
	data = reporter.process(data =
	[
		{
			'provider': 'appveyor',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'process'
		},
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	])
	assert 'Build of redaxmedia/chroma-feedback on appveyor in process' in data['message'][0]
	assert 'Build of redaxmedia/chroma-feedback on travis passed' in data['message'][1]
	assert data['status'] == 'process'


def test_process_errored():
	data = reporter.process(data =
	[
		{
			'provider': 'appveyor',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'errored'
		},
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	])
	assert 'Build of redaxmedia/chroma-feedback on appveyor errored' in data['message'][0]
	assert 'Build of redaxmedia/chroma-feedback on travis passed' in data['message'][1]
	assert data['status'] == 'errored'


def test_process_failed():
	data = reporter.process(data =
	[
		{
			'provider': 'appveyor',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'failed'
		},
		{
			'provider': 'circle',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'errored'
		},
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	])
	assert 'Build of redaxmedia/chroma-feedback on appveyor failed' in data['message'][0]
	assert 'Build of redaxmedia/chroma-feedback on circle errored' in data['message'][1]
	assert 'Build of redaxmedia/chroma-feedback on travis passed' in data['message'][2]
	assert data['status'] == 'failed'
