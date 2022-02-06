import importlib
import sys
from argparse import ArgumentParser
from typing import Any, List

from chroma_feedback import helper, logger, wording
from chroma_feedback.typing import Producer


def process(program : ArgumentParser) -> List[Producer]:
	args = helper.get_first(program.parse_known_args())
	result = []

	for producer_name in args.producer:
		producer = load_producer(producer_name)
		try:
			producer.init(program)
			result.extend(producer.run())
		except:
			logger.error(wording.get('producer_crashed').format(producer_name) + wording.get('exclamation_mark'))
			sys.exit()
	return result


def load_producer(producer_name : str) -> Any:
	try:
		return importlib.import_module('chroma_feedback.producer.' + producer_name)
	except ImportError:
		logger.error(wording.get('producer_not_found').format(producer_name) + wording.get('exclamation_mark'))
		sys.exit()
