from __future__ import print_function
import os
import sys
import threading
from src import provider, reporter, wording
from src.consumer import razer_chroma, system_tray

if sys.version_info < (3, 4):
	exit(wording.get('version_no').format(sys.version_info.major, sys.version_info.minor) + wording.get('exclamation_mark'))


def run(args):
	if threading.active_count() == 1:
		reporter.header()
		print()

	# process provider

	provider_result = provider.process(args)

	# handle exit

	if len(provider_result) == 0:
		exit(wording.get('provider_no') + wording.get('exclamation_mark'))

	# process reporter

	reporter_result = reporter.process(provider_result)
	if reporter_result:
		reporter.log(reporter_result)
		print()

	# handle dry run

	if args.dry_run is False:

		# process consumer

		consumer_result = razer_chroma.run(reporter_result['status'])
		if consumer_result:
			reporter.log(consumer_result)
			print()

	# handle thread

	if args.background_run is True:
		if threading.active_count() == 1:
			threading.Timer(args.background_interval, run, args =
			[
				args
			]).start()

			# handle system tray

			system_tray.run()
		if threading.active_count() > 1:
			system_tray.update(reporter_result['status'])


def destroy():
	print('\r' + wording.get('goodbye') + wording.get('exclamation_mark'))
	os._exit(0)
