import sys

from chroma_feedback import helper


def test_is_root() -> None:
	assert helper.is_root() is not None


def test_is_linux() -> None:
	assert helper.is_linux() is not None


def test_is_macos() -> None:
	assert helper.is_macos() is not None


def test_is_windows() -> None:
	assert helper.is_linux() is not None


def test_parse_slug() -> None:
	assert 'workspace' in helper.parse_slug('henryruhs')
	assert 'project' not in helper.parse_slug('henryruhs')
	assert 'workspace' in helper.parse_slug('henryruhs/chroma-feedback')
	assert 'project' in helper.parse_slug('henryruhs/chroma-feedback')
	assert 'workspace' not in helper.parse_slug(None)
	assert 'project' not in helper.parse_slug(None)


def test_create_description() -> None:
	assert helper.create_description('name', 'selector') == 'name [selector]'
	assert helper.create_description('name', None) == 'name'
	assert helper.create_description(None, 'selector') == 'selector'


def test_to_lower_case() -> None:
	assert helper.to_lower_case(None) == 'none'
	assert helper.to_lower_case('SUCCESS') == 'success'


def test_has_argument() -> None:
	sys.argv.clear()
	sys.argv.append('--valid')

	assert helper.has_argument('--valid') is True


def test_has_argument_invalid() -> None:
	sys.argv.clear()
	sys.argv.append('--invalid')

	assert helper.has_argument('--valid') is False


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


def test_remove_duplicate() -> None:
	assert helper.remove_duplicate(
	[
		1,
		1,
		2,
		2,
		3,
		3
	]) ==\
	[
		1,
		2,
		3
	]
