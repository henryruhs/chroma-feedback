from chroma_feedback import reporter


def test_create_provider_report_passed() -> None:
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


def test_create_provider_report_process() -> None:
	provider_report = reporter.create_provider_report(provider_result =
	[
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'process'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis in process' in provider_report[0]


def test_create_provider_report_errored() -> None:
	provider_report = reporter.create_provider_report(provider_result =
	[
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'errored'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis errored' in provider_report[0]


def test_create_provider_report_failed() -> None:
	provider_report = reporter.create_provider_report(provider_result =
	[
		{
			'provider': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'failed'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis failed' in provider_report[0]


def test_create_consumer_report_passed() -> None:
	consumer_report = reporter.create_consumer_report(consumer_result =
	[
		{
			'consumer': 'razer_chroma',
			'name': 'Razer Chroma',
			'active': True,
			'status': 'passed'
		}
	])

	assert 'Setting Razer Chroma to build passed' in consumer_report[0]


def test_create_consumer_report_process() -> None:
	consumer_report = reporter.create_consumer_report(consumer_result =
	[
		{
			'consumer': 'razer_chroma',
			'name': 'Razer Chroma',
			'active': True,
			'status': 'process'
		}
	])

	assert 'Setting Razer Chroma to build in process' in consumer_report[0]


def test_create_consumer_report_errored() -> None:
	consumer_report = reporter.create_consumer_report(consumer_result =
	[
		{
			'consumer': 'razer_chroma',
			'name': 'Razer Chroma',
			'active': True,
			'status': 'errored'
		}
	])

	assert 'Setting Razer Chroma to build errored' in consumer_report[0]


def test_create_consumer_report_failed() -> None:
	consumer_report = reporter.create_consumer_report(consumer_result =
	[
		{
			'consumer': 'razer_chroma',
			'name': 'Razer Chroma',
			'active': True,
			'status': 'failed'
		}
	])

	assert 'Setting Razer Chroma to build failed' in consumer_report[0]
