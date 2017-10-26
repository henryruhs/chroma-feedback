wordingArray =\
{
				'driver_no': 'Driver not found',
				'daemon_no': 'Daemon not found',
				'build_process': 'Build of {} in process',
				'build_passed': 'Build of {} passed',
				'build_failed': 'Build of {} failed',
				'setting_process': 'Setting {} to build in process',
				'setting_passed': 'Setting {} to build passed',
				'setting_failed': 'Setting {} to build failed',
				'goodbye': 'Goodbye',
				'divider': '-',
				'tick': u'\u2713',
				'cross': u'\u2715',
				'point': '.',
				'comma': ',',
				'colon': ':',
				'question_mark': '?',
				'exclamation_mark': '!'
}


def get(key):
	return wordingArray[key]
