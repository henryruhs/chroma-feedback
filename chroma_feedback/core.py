import signal
import sys
from argparse import ArgumentParser

from chroma_feedback import consumer, helper, logger, loop, metadata, producer, reporter, systray, wording

INTERVAL = 0


def cli() -> None:
	signal.signal(signal.SIGINT, lambda signal_number, frame: destroy())
	program = ArgumentParser()
	program.add_argument('-p', '--producer', action = 'append', choices = producer.ALL, required = True)
	program.add_argument('-c', '--consumer', action = 'append', choices = consumer.ALL, required = not helper.has_argument('-d') and not helper.has_argument('--dry-run'))
	program.add_argument('-b', '--background-run', action = 'store_true')
	program.add_argument('-i', '--background-interval', default = 60, type = int)
	program.add_argument('-d', '--dry-run', action = 'store_true')
	program.add_argument('-l', '--log-level', default = 'info', choices = logger.get_log_level())
	program.add_argument('-v', '--version', action = 'version', version = metadata.get('name') + ' ' + metadata.get('version'))
	init(program)


def init(program : ArgumentParser) -> None:
	args = helper.get_first(program.parse_known_args())
	logger.init(args.log_level)

	if sys.version_info < (3, 8):
		logger.error(wording.get('version_not_supported').format(sys.version_info.major, sys.version_info.minor) + wording.get('exclamation_mark'))
		sys.exit()

	reporter.print_header()
	application = loop.get_application()
	timer = loop.get_timer()
	timer.setInterval(100)
	if args.background_run:
		timer.timeout.connect(lambda: background_run(program))
	else:
		timer.timeout.connect(lambda: sys.exit())
	timer.singleShot(0, lambda: run(program))
	timer.start()
	sys.exit(application.exec())


def background_run(program : ArgumentParser) -> None:
	global INTERVAL

	args = helper.get_first(program.parse_known_args())
	timer = loop.get_timer()

	if INTERVAL == args.background_interval * 1000:
		run(program)
		INTERVAL = 0
	else:
		INTERVAL += timer.interval()


def run(program : ArgumentParser) -> None:
	args = helper.get_first(program.parse_known_args())
	producer_result = producer.process(program)

	if not producer_result:
		logger.error(wording.get('result_not_found') + wording.get('exclamation_mark'))
		sys.exit()

	producer_report = reporter.create_producer_report(producer_result)

	if producer_report:
		reporter.print_report(producer_report)

	if not args.dry_run:
		consumer_result = consumer.process(program, producer_report)
		consumer_report = reporter.create_consumer_report(consumer_result)

		if consumer_report:
			reporter.print_report(consumer_report)

	if args.background_run and loop.is_created():
		if systray.is_created():
			systray.update(producer_report)
		else:
			systray.create(producer_report)


def destroy() -> None:
	logger.info(wording.get('goodbye') + wording.get('exclamation_mark'))
	sys.exit()
