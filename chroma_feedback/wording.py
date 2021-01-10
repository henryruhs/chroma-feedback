WORDING =\
{
	'version_no': 'Python {}.{} not supported',
	'package_no': 'Package {} not found',
	'connection_no': 'Connection to {} not found',
	'daemon_no': 'Daemon for {} not found',
	'ip_no': 'IP for {} not found',
	'device_no': 'Device not found',
	'light_no': 'Light not found',
	'group_no': 'Group not found',
	'producer_no': 'Producer {} not found',
	'producer_crash': 'Producer {} crashed',
	'consumer_no': 'Consumer {} not found',
	'consumer_crash': 'Consumer {} crashed',
	'result_no': 'Result not found',
	'build_passed': 'Build of {} on {} passed',
	'build_started': 'Build of {} on {} started',
	'build_errored': 'Build of {} on {} errored',
	'build_failed': 'Build of {} on {} failed',
	'setting_passed': 'Setting {} to build passed',
	'setting_started': 'Setting {} to build started',
	'setting_errored': 'Setting {} to build errored',
	'setting_failed': 'Setting {} to build failed',
	'press_button': 'Press {} button on {}',
	'enable_feature': 'Enable {} on {}',
	'goodbye': 'Goodbye',
	'about': 'About',
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
