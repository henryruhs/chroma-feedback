from chroma_feedback import color


def test_format_red() -> None:
	assert color.format_red('__test__') == '\033[0;31m__test__\033[0m'


def test_format_green() -> None:
	assert color.format_green('__test__') == '\033[0;32m__test__\033[0m'


def test_format_yellow() -> None:
	assert color.format_yellow('__test__') == '\033[0;33m__test__\033[0m'


def test_get_passed() -> None:
	state = color.get_passed()

	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state


def test_get_process() -> None:
	state = color.get_process()

	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state


def test_get_errored() -> None:
	state = color.get_errored()

	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state


def test_get_failed() -> None:
	state = color.get_failed()

	assert 'rgb' in state
	assert 'hue' in state
	assert 'saturation' in state
	assert 'brightness' in state
	assert 'kelvin' in state
