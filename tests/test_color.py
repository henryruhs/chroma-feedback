from chroma_feedback import color


def test_format_red() -> None:
	assert color.format_red('__test__') == '\033[0;31m__test__\033[0m'

def test_format_orange() -> None:
	assert color.format_orange('__test__') == '\033[38:2:255:165:0m__test__\033[0m'


def test_format_green() -> None:
	assert color.format_green('__test__') == '\033[0;32m__test__\033[0m'


def test_format_yellow() -> None:
	assert color.format_yellow('__test__') == '\033[0;33m__test__\033[0m'


def test_get_passed() -> None:
	state = color.get_passed()

	assert 'name' in state
	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state


def test_get_process() -> None:
	state = color.get_process()

	assert 'name' in state
	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state


def test_get_warning() -> None:
	state = color.get_warning()

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


def test_get_failed() -> None:
	state = color.get_failed()

	assert 'name' in state
	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state
