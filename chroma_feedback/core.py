from __future__ import print_function
from typing import Any
from argparse import ArgumentParser
import os
import sys
import threading
from chroma_feedback import consumer, helper, producer, reporter, wording
if helper.is_linux():
	from chroma_feedback import systray


def run(program : ArgumentParser) -> None:
	status = None

	if sys.version_info < (3, 4):
		exit(wording.get('version_no').format(sys.version_info.major, sys.version_info.minor) + wording.get('exclamation_mark'))

	# report header

	if threading.active_count() == 1:
		reporter.print_header()
		print()

	# process producer

	producer_result = producer.process(program)

	# handle exit

	if not producer_result:
		exit(wording.get('result_no') + wording.get('exclamation_mark'))

	# report producer

	producer_report = reporter.create_producer_report(producer_result)
	if producer_report:
		reporter.print_report(producer_report)
		print()

	# handle dry run

	args = helper.get_first(program.parse_known_args())
	if args.dry_run is False:

		# process consumer

		status = helper.get_producer_status(producer_result)
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
		if helper.is_linux():
			systray_report = reporter.create_systray_report(producer_result)
			if systray.is_active():
				systray.update(status, systray_report)
			else:
				systray.create(status, systray_report)


def destroy(signal_number : int, frame : Any) -> None:
	print('\r' + wording.get('goodbye') + wording.get('exclamation_mark'))
	os._exit(0)
