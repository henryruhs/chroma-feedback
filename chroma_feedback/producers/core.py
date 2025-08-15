import importlib
import sys
from argparse import ArgumentParser
from types import ModuleType
from typing import List

from chroma_feedback import logger, producers, wording
from chroma_feedback.types import Producer


def process(program : ArgumentParser) -> List[Producer]:
	args, _ = program.parse_known_args()
	result = []

	for producer_name in args.producer:
		producer = load_producer(producer_name)

		try:
			producer.init(program)
			result.extend(producer.run())
		except Exception as exception:
			logger.debug(str(exception))
			logger.error(wording.get('producer_crashed').format(producer_name) + wording.get('exclamation_mark'))
			sys.exit()
	return result


def load_producer(producer_name : str) -> ModuleType:
	try:
		return importlib.import_module(producers.ALL[producer_name])
	except ModuleNotFoundError:
		logger.error(wording.get('producer_not_found').format(producers.ALL[producer_name]) + wording.get('exclamation_mark'))
		sys.exit()
