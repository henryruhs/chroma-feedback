from __future__ import print_function
from typing import Any
from argparse import ArgumentParser
import os
import sys
import threading
from chroma_feedback import consumer, helper, provider, reporter, wording


def run(program : ArgumentParser) -> None:
	if sys.version_info < (3, 4):
		exit(wording.get('version_no').format(sys.version_info.major, sys.version_info.minor) + wording.get('exclamation_mark'))

	# report header

	if threading.active_count() == 1:
		reporter.print_header()
		print()

	# process provider

	provider_result = provider.process(program)

	# handle exit

	if not provider_result:
		exit(wording.get('result_no') + wording.get('exclamation_mark'))

	# report provider

	provider_report = reporter.create_provider_report(provider_result)
	if provider_report:
		reporter.print_report(provider_report)
		print()

	# handle dry run

	args = helper.get_first(program.parse_known_args())
	if args.dry_run is False:

		# process consumer

		status = helper.get_provider_status(provider_result)
		consumer_result = consumer.process(program, status)

		# report consumer

		consumer_report = reporter.create_consumer_report(consumer_result)
		if consumer_report:
			reporter.print_report(consumer_report)
			print()

	# handle thread

	if args.background_run is True:
		threading.Timer(args.background_interval, run, args =
		[
			program
		]).start()


def destroy(signal_number : int, frame : Any) -> None:
	print('\r' + wording.get('goodbye') + wording.get('exclamation_mark'))
	os._exit(0)
