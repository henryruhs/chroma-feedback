import importlib
import sys
from argparse import ArgumentParser
from typing import Any, List

from chroma_feedback import consumer, helper, logger, wording
from chroma_feedback.typing import Consumer, ProducerReport


def process(program : ArgumentParser, producer_report : List[ProducerReport]) -> List[Consumer]:
	args = helper.get_first(program.parse_known_args())
	result = []

	for consumer_name in args.consumer:
		consumer = load_consumer(consumer_name)

		if consumer.support():
			try:
				consumer.init(program)
				result.extend(consumer.run(producer_report))
			except Exception as exception:
				logger.debug(str(exception))
				logger.error(wording.get('consumer_crashed').format(consumer_name) + wording.get('exclamation_mark'))
				sys.exit()
		else:
			logger.error(wording.get('consumer_not_supported').format(consumer_name) + wording.get('exclamation_mark'))
			sys.exit()
	return result


def load_consumer(consumer_name : str) -> Any:
	try:
		return importlib.import_module(consumer.ALL[consumer_name])
	except ImportError:
		logger.error(wording.get('consumer_not_found').format(consumer.ALL[consumer_name]) + wording.get('exclamation_mark'))
		sys.exit()
