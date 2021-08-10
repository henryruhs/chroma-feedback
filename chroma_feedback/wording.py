WORDING =\
{
	'version_not_supported': 'Python {}.{} not supported',
	'package_not_found': 'Package {} not found',
	'connection_not_found': 'Connection to {} not found',
	'daemon_not_found': 'Daemon for {} not found',
	'ip_not_found': 'IP for {} not found',
	'device_not_found': 'Device not found',
	'light_not_found': 'Light not found',
	'group_not_found': 'Group not found',
	'producer_not_found': 'Producer {} not found',
	'producer_crashed': 'Producer {} crashed',
	'consumer_not_supported': 'Consumer {} not supported',
	'consumer_not_found': 'Consumer {} not found',
	'consumer_crashed': 'Consumer {} crashed',
	'result_not_found': 'Result not found',
	'build_passed': 'Build of {} on {} passed',
	'build_started': 'Build of {} on {} started',
	'build_errored': 'Build of {} on {} errored',
	'build_failed': 'Build of {} on {} failed',
	'set_passed': 'Set {} state to passed',
	'set_started': 'Set {} state to started',
	'set_errored': 'Set {} state to errored',
	'set_failed': 'Set {} state to failed',
	'press_button': 'Press {} button on {}',
	'enable_feature': 'Enable {} on {}',
	'goodbye': 'Goodbye',
	'start': 'Start',
	'stop': 'Stop',
	'exit': 'Exit',
	'by': 'by',
	'hourglass': u'\u29d7',
	'tick': u'\u2714',
	'cross': u'\u2716',
	'point': '.',
	'comma': ',',
	'colon': ':',
	'question_mark': '?',
	'exclamation_mark': '!'
}


def get(key : str) -> str:
	return WORDING[key]
