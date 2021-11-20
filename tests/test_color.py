from chroma_feedback import color


def test_format_passed() -> None:
	assert color.format_passed('__test__') == '\033[0;32m__test__\033[0m'


def test_format_started() -> None:
	assert color.format_started('__test__') == '\033[0;34m__test__\033[0m'


def test_format_warned() -> None:
	assert color.format_warned('__test__') == '\033[0;33m__test__\033[0m'


def test_format_failed() -> None:
	assert color.format_failed('__test__') == '\033[0;31m__test__\033[0m'


def test_get_passed() -> None:
	state = color.get_passed()

	assert 'name' in state
	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state


def test_get_started() -> None:
	state = color.get_started()

	assert 'name' in state
	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state


def test_get_errored() -> None:
	state = color.get_errored()

	assert 'name' in state
	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state


def test_get_warned() -> None:
	state = color.get_warned()

	assert 'name' in state
	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state


def test_get_failed() -> None:
	state = color.get_failed()

	assert 'name' in state
	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state
