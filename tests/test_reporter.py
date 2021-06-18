from chroma_feedback import reporter


def test_create_producer_report_passed() -> None:
	producer_report = reporter.create_producer_report(
	[
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	])

	assert producer_report[0]['status'] == 'passed'
	assert producer_report[0]['message'] == 'Build of redaxmedia/chroma-feedback on github passed'
	assert producer_report[0]['symbol']


def test_create_producer_report_started() -> None:
	producer_report = reporter.create_producer_report(
	[
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'started'
		}
	])

	assert producer_report[0]['status'] == 'started'
	assert producer_report[0]['message'] == 'Build of redaxmedia/chroma-feedback on github started'
	assert producer_report[0]['symbol']


def test_create_producer_report_errored() -> None:
	producer_report = reporter.create_producer_report(
	[
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'errored'
		}
	])

	assert producer_report[0]['status'] == 'errored'
	assert producer_report[0]['message'] == 'Build of redaxmedia/chroma-feedback on github errored'
	assert producer_report[0]['symbol']


def test_create_producer_report_failed() -> None:
	producer_report = reporter.create_producer_report(
	[
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'failed'
		}
	])

	assert producer_report[0]['status'] == 'failed'
	assert producer_report[0]['message'] == 'Build of redaxmedia/chroma-feedback on github failed'
	assert producer_report[0]['symbol']


def test_create_consumer_report_passed() -> None:
	consumer_report = reporter.create_consumer_report(
	[
		{
			'consumer': 'razer_chroma',
			'type': 'device',
			'name': 'Razer Chroma',
			'active': True,
			'status': 'passed'
		}
	])

	assert consumer_report[0]['status'] == 'passed'
	assert consumer_report[0]['message'] == 'Setting Razer Chroma to build passed'
	assert consumer_report[0]['symbol']



def test_create_consumer_report_started() -> None:
	consumer_report = reporter.create_consumer_report(
	[
		{
			'consumer': 'razer_chroma',
			'type': 'device',
			'name': 'Razer Chroma',
			'active': True,
			'status': 'started'
		}
	])

	assert consumer_report[0]['status'] == 'started'
	assert consumer_report[0]['message'] == 'Setting Razer Chroma to build started'
	assert consumer_report[0]['symbol']


def test_create_consumer_report_errored() -> None:
	consumer_report = reporter.create_consumer_report(
	[
		{
			'consumer': 'razer_chroma',
			'type': 'device',
			'name': 'Razer Chroma',
			'active': True,
			'status': 'errored'
		}
	])

	assert consumer_report[0]['status'] == 'errored'
	assert consumer_report[0]['message'] == 'Setting Razer Chroma to build errored'
	assert consumer_report[0]['symbol']


def test_create_consumer_report_failed() -> None:
	consumer_report = reporter.create_consumer_report(
	[
		{
			'consumer': 'razer_chroma',
			'type': 'device',
			'name': 'Razer Chroma',
			'active': True,
			'status': 'failed'
		}
	])

	assert consumer_report[0]['status'] == 'failed'
	assert consumer_report[0]['message'] == 'Setting Razer Chroma to build failed'
	assert consumer_report[0]['symbol']
