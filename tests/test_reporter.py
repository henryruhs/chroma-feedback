from chroma_feedback import reporter


def test_create_producer_report_passed() -> None:
	producer_report = reporter.create_producer_report(producer_result =
	[
		{
			'producer': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis passed' in producer_report[0]


def test_create_producer_report_started() -> None:
	producer_report = reporter.create_producer_report(producer_result =
	[
		{
			'producer': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'started'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis started' in producer_report[0]


def test_create_producer_report_errored() -> None:
	producer_report = reporter.create_producer_report(producer_result =
	[
		{
			'producer': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'errored'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis errored' in producer_report[0]


def test_create_producer_report_failed() -> None:
	producer_report = reporter.create_producer_report(producer_result =
	[
		{
			'producer': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'failed'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis failed' in producer_report[0]


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


def test_create_consumer_report_started() -> None:
	consumer_report = reporter.create_consumer_report(consumer_result =
	[
		{
			'consumer': 'razer_chroma',
			'name': 'Razer Chroma',
			'active': True,
			'status': 'started'
		}
	])

	assert 'Setting Razer Chroma to build started' in consumer_report[0]


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


def test_create_systray_report_passed() -> None:
	systray_report = reporter.create_systray_report(producer_result =
	[
		{
			'producer': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis passed' in systray_report[0]


def test_create_systray_report_started() -> None:
	systray_report = reporter.create_systray_report(producer_result =
	[
		{
			'producer': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'started'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis started' in systray_report[0]


def test_create_systray_report_errored() -> None:
	systray_report = reporter.create_systray_report(producer_result =
	[
		{
			'producer': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'errored'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis errored' in systray_report[0]


def test_create_systray_report_failed() -> None:
	systray_report = reporter.create_systray_report(producer_result =
	[
		{
			'producer': 'travis',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'failed'
		}
	])

	assert 'Build of redaxmedia/chroma-feedback on travis failed' in systray_report[0]
