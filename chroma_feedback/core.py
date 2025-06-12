import signal
import sys
from argparse import ArgumentParser
from functools import partial
from types import FrameType

from chroma_feedback import consumer, helper, logger, loop, metadata, producer, reporter, systray, wording

INTERVAL = 0


def cli() -> None:
	signal.signal(signal.SIGINT, signal_exit)
	program = ArgumentParser(add_help = False)
	program.add_argument('-p', '--producer', action = 'append', choices = producer.ALL, required = True)
	program.add_argument('-c', '--consumer', action = 'append', choices = consumer.ALL, required = not helper.has_argument('-d') and not helper.has_argument('--dry-run'))
	program.add_argument('-b', '--background-run', action = 'store_true')
	program.add_argument('-i', '--background-interval', default = 60, type = int)
	program.add_argument('-d', '--dry-run', action = 'store_true')
	program.add_argument('-l', '--log-level', default = 'info', choices = logger.get_log_levels())
	program.add_argument('-v', '--version', version = metadata.get('name') + ' ' + metadata.get('version'), action = 'version')
	init(program)


def init(program : ArgumentParser) -> None:
	args, _ = program.parse_known_args()
	logger.init(args.log_level)

	if sys.version_info < (3, 10):
		logger.error(wording.get('version_not_supported').format(sys.version_info.major, sys.version_info.minor) + wording.get('exclamation_mark'))
		sys.exit()

	reporter.print_header()
	application = loop.get_application()
	timer = loop.get_timer()
	timer.setInterval(100)
	if args.background_run:
		timer.timeout.connect(partial(background_run, program))
	else:
		timer.timeout.connect(partial(sys.exit))
	timer.singleShot(0, partial(run, program))
	timer.start()
	sys.exit(application.exec())


def background_run(program : ArgumentParser) -> None:
	global INTERVAL

	args, _ = program.parse_known_args()
	timer = loop.get_timer()

	if INTERVAL == args.background_interval * 1000:
		run(program)
		INTERVAL = 0
	else:
		INTERVAL += timer.interval()


def run(program : ArgumentParser) -> None:
	args, _ = program.parse_known_args()
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


def signal_exit(signum : int, frame : FrameType) -> None:
	graceful_exit()


def graceful_exit() -> None:
	logger.info(wording.get('goodbye') + wording.get('exclamation_mark'))
	signal.signal(signal.SIGINT, signal.SIG_IGN)
	sys.exit(0)
