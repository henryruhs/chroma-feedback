from chroma_feedback import helper


def test_get_producer_status_started() -> None:
	assert helper.get_producer_status(
	[
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'started'
		},
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	]) is 'started'


def test_get_producer_status_errored() -> None:
	assert helper.get_producer_status(
	[
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'errored'
		},
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'started'
		},
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	]) is 'errored'


def test_get_producer_status_failed() -> None:
	assert helper.get_producer_status(
	[
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'failed'
		},
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'started'
		},
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'errored'
		},
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		},
	]) is 'failed'


def test_get_producer_status_passed() -> None:
	assert helper.get_producer_status(
	[
		{
			'producer': 'github',
			'slug': 'redaxmedia/chroma-feedback',
			'active': True,
			'status': 'passed'
		}
	]) is 'passed'


def test_parse_slug() -> None:
	assert 'workspace' in helper.parse_slug('redaxmedia')
	assert 'project' not in helper.parse_slug('redaxmedia')
	assert 'workspace' in helper.parse_slug('redaxmedia/chroma-feedback')
	assert 'project' in helper.parse_slug('redaxmedia/chroma-feedback')
	assert 'workspace' not in helper.parse_slug(None)
	assert 'project' not in helper.parse_slug(None)


def test_is_root() -> None:
	assert helper.is_root() is not None


def test_is_linux() -> None:
	assert helper.is_linux() is not None


def test_is_windows() -> None:
	assert helper.is_linux() is not None


def test_to_lower_case() -> None:
	assert helper.to_lower_case(None) == 'none'
	assert helper.to_lower_case('SUCCESS') == 'success'


def test_has_argument() -> None:
	assert helper.has_argument('invalid') is False


def test_get_first() -> None:
	assert helper.get_first(
	[
		1,
		2,
		3
	]) == 1


def test_get_last() -> None:
	assert helper.get_last(
	[
		1,
		2,
		3
	]) == 3
