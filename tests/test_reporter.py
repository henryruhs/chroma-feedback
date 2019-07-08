from src import reporter


def test_create_provider_report_passed():
	reporter_result = reporter.create_provider_report(provider_result =
	[
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis passed' in reporter_result['message'][0]


def test_create_provider_report_process():
	reporter_result = reporter.create_provider_report(provider_result =
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
			'status': 'process'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on appveyor errored' in reporter_result['message'][0]
	assert 'Build of redaxmedia/chroma-feedback on travis in process' in reporter_result['message'][1]


def test_create_provider_report_errored():
	reporter_result = reporter.create_provider_report(provider_result =
	[
		{
			'provider': 'appveyor',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'failed'
		},
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'errored'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on appveyor failed' in reporter_result['message'][0]
	assert 'Build of redaxmedia/chroma-feedback on travis errored' in reporter_result['message'][1]


def test_create_provider_report_failed():
	reporter_result = reporter.create_provider_report(provider_result =
	[
		{
			'provider': 'appveyor',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'failed'
		},
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on appveyor failed' in reporter_result['message'][0]
	assert 'Build of redaxmedia/chroma-feedback on travis passed' in reporter_result['message'][1]
