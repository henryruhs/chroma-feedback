wording =\
{
	'driver_no': 'Driver not found',
	'daemon_no': 'Daemon not found',
	'device_no': 'Device not found',
	'data_no': 'Data not found',
	'build_passed': 'Build of {} on {} passed',
	'build_process': 'Build of {} on {} in process',
	'build_errored': 'Build of {} on {} errored',
	'build_failed': 'Build of {} on {} failed',
	'setting_passed': 'Setting {} to build passed',
	'setting_process': 'Setting {} to build in process',
	'setting_errored': 'Setting {} to build errored',
	'setting_failed': 'Setting {} to build failed',
	'goodbye': 'Goodbye',
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


def get(key):
	return wording[key]
