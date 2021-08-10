from __future__ import print_function
import signal
import sys
from argparse import ArgumentParser
from chroma_feedback import consumer, helper, loop, metadata, producer, systray, reporter, wording

INTERVAL = 0


def cli() -> None:
	signal.signal(signal.SIGINT, lambda signal_number, frame: destroy())
	program = ArgumentParser()
	program.add_argument('-V', '--version', action = 'version', version = metadata.get('name') + ' ' + metadata.get('version'))
	program.add_argument('-P', '--producer', action = 'append', choices = producer.__all__, required = True)
	program.add_argument('-C', '--consumer', action = 'append', choices = consumer.__all__, required = helper.has_argument('--dry-run') is False)
	program.add_argument('-I', '--background-interval', default = 60, type = int)
	program.add_argument('-B', '--background-run', action = 'store_true')
	program.add_argument('-D', '--dry-run', action = 'store_true')
	init(program)


def init(program : ArgumentParser) -> None:
	args = helper.get_first(program.parse_known_args())

	if sys.version_info < (3, 8):
		sys.exit(wording.get('version_not_supported').format(sys.version_info.major, sys.version_info.minor) + wording.get('exclamation_mark'))

	# report header

	reporter.print_header()
	print()

	# handle background run

	if args.background_run is True:
		application = loop.get_application()
		timer = loop.get_timer()
		timer.setInterval(500)
		timer.timeout.connect(lambda: background_run(program))
		timer.singleShot(0, lambda: run(program)) # type: ignore
		timer.start()
		sys.exit(application.exec_())
	else:
		run(program)


def background_run(program : ArgumentParser) -> None:
	global INTERVAL

	args = helper.get_first(program.parse_known_args())
	timer = loop.get_timer()

	# handle interval

	if INTERVAL == args.background_interval * 1000:
		run(program)
		INTERVAL = 0
	else:
		INTERVAL += timer.interval()


def run(program : ArgumentParser) -> None:
	args = helper.get_first(program.parse_known_args())
	status = None

	# process producer

	producer_result = producer.process(program)

	# handle exit

	if not producer_result:
		sys.exit(wording.get('result_not_found') + wording.get('exclamation_mark'))

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

	if loop.is_created() is True:
		if systray.is_created() is True:
			systray.update(status, producer_report)
		else:
			systray.create(status, producer_report)


def destroy() -> None:
	print()
	sys.exit(wording.get('goodbye') + wording.get('exclamation_mark'))
