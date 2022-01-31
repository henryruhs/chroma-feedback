from chroma_feedback import reporter


def test_create_producer_report_passed() -> None:
	producer_report = reporter.create_producer_report(
	[
		{
			'name': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'url': 'https://github.com/redaxmedia/chroma-feedback',
			'status': 'passed'
		}
	])

	assert producer_report[0]['symbol']
	assert producer_report[0]['message'] == 'Status of redaxmedia/chroma-feedback on github is passed'
	assert producer_report[0]['url'] == 'https://github.com/redaxmedia/chroma-feedback'
	assert producer_report[0]['status'] == 'passed'


def test_create_producer_report_started() -> None:
	producer_report = reporter.create_producer_report(
	[
		{
			'name': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'url': 'https://github.com/redaxmedia/chroma-feedback',
			'status': 'started'
		}
	])

	assert producer_report[0]['symbol']
	assert producer_report[0]['message'] == 'Status of redaxmedia/chroma-feedback on github is started'
	assert producer_report[0]['url'] == 'https://github.com/redaxmedia/chroma-feedback'
	assert producer_report[0]['status'] == 'started'


def test_create_producer_report_errored() -> None:
	producer_report = reporter.create_producer_report(
	[
		{
			'name': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'url': 'https://github.com/redaxmedia/chroma-feedback',
			'status': 'errored'
		}
	])

	assert producer_report[0]['symbol']
	assert producer_report[0]['message'] == 'Status of redaxmedia/chroma-feedback on github is errored'
	assert producer_report[0]['url'] == 'https://github.com/redaxmedia/chroma-feedback'
	assert producer_report[0]['status'] == 'errored'


def test_create_producer_report_warned() -> None:
	producer_report = reporter.create_producer_report(
	[
		{
			'name': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'url': 'https://github.com/redaxmedia/chroma-feedback',
			'status': 'warned'
		}
	])

	assert producer_report[0]['symbol']
	assert producer_report[0]['message'] == 'Status of redaxmedia/chroma-feedback on github is warned'
	assert producer_report[0]['url'] == 'https://github.com/redaxmedia/chroma-feedback'
	assert producer_report[0]['status'] == 'warned'


def test_create_producer_report_failed() -> None:
	producer_report = reporter.create_producer_report(
	[
		{
			'name': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'url': 'https://github.com/redaxmedia/chroma-feedback',
			'status': 'failed'
		}
	])

	assert producer_report[0]['symbol']
	assert producer_report[0]['message'] == 'Status of redaxmedia/chroma-feedback on github is failed'
	assert producer_report[0]['status'] == 'failed'


def test_create_consumer_report_passed() -> None:
	consumer_report = reporter.create_consumer_report(
	[
		{
			'name': 'razer_chroma',
			'type': 'device',
			'description': 'Razer Huntsman Elite',
			'status': 'passed'
		}
	])

	assert consumer_report[0]['symbol']
	assert consumer_report[0]['message'] == 'Set status of Razer Huntsman Elite to passed'
	assert consumer_report[0]['status'] == 'passed'



def test_create_consumer_report_started() -> None:
	consumer_report = reporter.create_consumer_report(
	[
		{
			'name': 'razer_chroma',
			'type': 'device',
			'description': 'Razer Huntsman Elite',
			'status': 'started'
		}
	])

	assert consumer_report[0]['symbol']
	assert consumer_report[0]['message'] == 'Set status of Razer Huntsman Elite to started'
	assert consumer_report[0]['status'] == 'started'


def test_create_consumer_report_errored() -> None:
	consumer_report = reporter.create_consumer_report(
	[
		{
			'name': 'razer_chroma',
			'type': 'device',
			'description': 'Razer Huntsman Elite',
			'status': 'errored'
		}
	])

	assert consumer_report[0]['symbol']
	assert consumer_report[0]['message'] == 'Set status of Razer Huntsman Elite to errored'
	assert consumer_report[0]['status'] == 'errored'


def test_create_consumer_report_warned() -> None:
	consumer_report = reporter.create_consumer_report(
	[
		{
			'name': 'razer_chroma',
			'type': 'device',
			'description': 'Razer Huntsman Elite',
			'status': 'warned'
		}
	])

	assert consumer_report[0]['symbol']
	assert consumer_report[0]['message'] == 'Set status of Razer Huntsman Elite to warned'
	assert consumer_report[0]['status'] == 'warned'


def test_create_consumer_report_failed() -> None:
	consumer_report = reporter.create_consumer_report(
	[
		{
			'name': 'razer_chroma',
			'type': 'device',
			'description': 'Razer Huntsman Elite',
			'status': 'failed'
		}
	])

	assert consumer_report[0]['symbol']
	assert consumer_report[0]['message'] == 'Set status of Razer Huntsman Elite to failed'
	assert consumer_report[0]['status'] == 'failed'


def test_resolve_report_status_started() -> None:
	assert reporter.resolve_report_status(
	[
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'started'
		},
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'passed'
		}
	]) == 'started'


def test_resolve_report_status_errored() -> None:
	assert reporter.resolve_report_status(
	[
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'errored'
		},
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'started'
		},
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'passed'
		}
	]) == 'errored'


def test_resolve_report_status_warned() -> None:
	assert reporter.resolve_report_status(
	[
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'warned'
		},
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'errored'
		},
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'started'
		},
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'passed'
		}
	]) == 'warned'


def test_get_producer_status_failed() -> None:
	assert reporter.resolve_report_status(
	[
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'failed'
		},
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'warned'
		},
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'started'
		},
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'errored'
		},
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'passed'
		},
	]) == 'failed'


def test_get_producer_status_passed() -> None:
	assert reporter.resolve_report_status(
	[
		{
			'name': 'github',
			'symbol': None,
			'message': None,
			'url': 'https://github.com/redaxmedia/chroma-feedback/actions/runs/1',
			'status': 'passed'
		}
	]) == 'passed'
