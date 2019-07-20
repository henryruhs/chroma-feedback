from chroma_feedback import color


def test_red():
	assert color.red('__test__') == '\033[0;31m__test__\033[0m'


def test_green():
	assert color.green('__test__') == '\033[0;32m__test__\033[0m'


def test_yellow():
	assert color.yellow('__test__') == '\033[0;33m__test__\033[0m'


def test_get_passed_rgb():
	state = color.get_passed_rgb()

	assert 'red' in state
	assert 'green' in state
	assert 'blue' in state


def test_get_process_rgb():
	state = color.get_process_rgb()

	assert 'red' in state
	assert 'green' in state
	assert 'blue' in state


def test_get_errored_rgb():
	state = color.get_errored_rgb()

	assert 'red' in state
	assert 'green' in state
	assert 'blue' in state


def test_get_failed_rgb():
	state = color.get_failed_rgb()

	assert 'red' in state
	assert 'green' in state
	assert 'blue' in state


def test_get_passed_hue():
	state = color.get_passed_hue()

	assert 'hue' in state
	assert 'saturation' in state


def test_get_process_hue():
	state = color.get_process_hue()

	assert 'hue' in state
	assert 'saturation' in state


def test_get_errored_hue():
	state = color.get_errored_hue()

	assert 'hue' in state
	assert 'saturation' in state


def test_get_failed_hue():
	state = color.get_failed_hue()

	assert 'hue' in state
	assert 'saturation' in state
