import src.reporter as reporter


def test_process_data_passed():
	data = reporter.process_data(data =
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


def test_process_data_process():
	data = reporter.process_data(data =
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


def test_process_data_errored():
	data = reporter.process_data(data =
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


def test_process_data_failed():
	data = reporter.process_data(data =
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
