from __future__ import print_function
import os
import sys
import threading
from src import consumer, provider, reporter, wording


def run(program):
	if sys.version_info < (3, 4):
		exit(wording.get('version_no').format(sys.version_info.major, sys.version_info.minor) + wording.get('exclamation_mark'))

	# print header

	if threading.active_count() == 1:
		reporter.header()
		print()

	# process provider

	provider_result = provider.process(program)

	# handle exit

	if not provider_result:
		exit(wording.get('result_no') + wording.get('exclamation_mark'))

	# print summary

	reporter_result = reporter.process(provider_result)
	if reporter_result:
		reporter.summary(reporter_result)
		print()

	# handle dry run

	args = program.parse_known_args()[0]
	if args.dry_run is False:

		# process consumer

		consumer_result = consumer.process(reporter_result, program)

		# print summary

		if consumer_result:
			print(consumer_result)
			reporter.summary(consumer_result)
			print()

	# handle thread

	if args.background_run is True:
		if threading.active_count() == 1:
			threading.Timer(args.background_interval, run, args =
			[
				args
			]).start()


def destroy(number, frame):
	print('\r' + wording.get('goodbye') + wording.get('exclamation_mark'))
	os._exit(0)
