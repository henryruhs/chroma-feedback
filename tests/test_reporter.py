from src import reporter


def test_create_provider_report_passed():
	provider_report = reporter.create_provider_report(provider_result =
	[
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis passed' in provider_report[0]


def test_create_provider_report_process():
	provider_report = reporter.create_provider_report(provider_result =
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

	assert 'Build of redaxmedia/chroma-feedback on appveyor errored' in provider_report[0]
	assert 'Build of redaxmedia/chroma-feedback on travis in process' in provider_report[1]


def test_create_provider_report_errored():
	provider_report = reporter.create_provider_report(provider_result =
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

	assert 'Build of redaxmedia/chroma-feedback on appveyor failed' in provider_report[0]
	assert 'Build of redaxmedia/chroma-feedback on travis errored' in provider_report[1]


def test_create_provider_report_failed():
	provider_report = reporter.create_provider_report(provider_result =
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

	assert 'Build of redaxmedia/chroma-feedback on appveyor failed' in provider_report[0]
	assert 'Build of redaxmedia/chroma-feedback on travis passed' in provider_report[1]
