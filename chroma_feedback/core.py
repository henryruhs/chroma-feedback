from __future__ import print_function
import sys
from argparse import ArgumentParser
from chroma_feedback import consumer, helper, loop, producer, systray, reporter, wording


def init(program : ArgumentParser) -> None:
	args = helper.get_first(program.parse_known_args())

	if sys.version_info < (3, 8):
		sys.exit(wording.get('version_no').format(sys.version_info.major, sys.version_info.minor) + wording.get('exclamation_mark'))

	# report header

	reporter.print_header()
	print()

	# handle background run

	if args.background_run is True:
		application = loop.get_application()
		timer = loop.get_timer()
		timer.setInterval(args.background_interval * 1000)
		timer.timeout.connect(lambda: run(program))
		timer.singleShot(0, lambda: run(program)) # type: ignore
		timer.start()
		sys.exit(application.exec_())
	else:
		run(program)


def run(program : ArgumentParser) -> None:
	args = helper.get_first(program.parse_known_args())
	status = None

	# process producer

	producer_result = producer.process(program)

	# handle exit

	if not producer_result:
		sys.exit(wording.get('result_no') + wording.get('exclamation_mark'))

	# report producer

	producer_report = reporter.create_producer_report(producer_result)

	if producer_report:
		reporter.print_report(producer_report)
		print()

	# handle dry run

	if args.dry_run is False:

		# process consumer

		status = helper.get_producer_status(producer_result)
		consumer_result = consumer.process(program, status)

		# report consumer

		consumer_report = reporter.create_consumer_report(consumer_result)

		if consumer_report:
			reporter.print_report(consumer_report)
			print()

	# handle systray

	if loop.is_active() is True:
		systray_report = reporter.create_systray_report(producer_result)

		if systray.is_active() is True:
			systray.update(status, systray_report)
		else:
			systray.create(status, systray_report)


def destroy() -> None:
	print()
	sys.exit(wording.get('goodbye') + wording.get('exclamation_mark'))
