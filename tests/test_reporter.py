from src import reporter


def test_process_passed():
	reporter_result = reporter.process(provider_result =
	[
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	])
	assert 'Build of redaxmedia/chroma-feedback on travis passed' in reporter_result['message'][0]
	assert reporter_result['status'] == 'passed'


def test_process_process():
	reporter_result = reporter.process(provider_result =
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
	assert 'Build of redaxmedia/chroma-feedback on appveyor in process' in reporter_result['message'][0]
	assert 'Build of redaxmedia/chroma-feedback on travis passed' in reporter_result['message'][1]
	assert reporter_result['status'] == 'process'


def test_process_errored():
	reporter_result = reporter.process(provider_result =
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
	assert 'Build of redaxmedia/chroma-feedback on appveyor errored' in reporter_result['message'][0]
	assert 'Build of redaxmedia/chroma-feedback on travis passed' in reporter_result['message'][1]
	assert reporter_result['status'] == 'errored'


def test_process_failed():
	reporter_result = reporter.process(provider_result =
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
	assert 'Build of redaxmedia/chroma-feedback on appveyor failed' in reporter_result['message'][0]
	assert 'Build of redaxmedia/chroma-feedback on circle errored' in reporter_result['message'][1]
	assert 'Build of redaxmedia/chroma-feedback on travis passed' in reporter_result['message'][2]
	assert reporter_result['status'] == 'failed'
