from chroma_feedback import color


def test_red():
	assert color.red('__test__') == '\033[0;31m__test__\033[0m'


def test_green():
	assert color.green('__test__') == '\033[0;32m__test__\033[0m'


def test_yellow():
	assert color.yellow('__test__') == '\033[0;33m__test__\033[0m'
