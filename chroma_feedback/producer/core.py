from typing import Any, List
import sys
from argparse import ArgumentParser
import importlib
from chroma_feedback import helper, wording
from chroma_feedback.typing import ProducerModel


def process(program : ArgumentParser) -> List[ProducerModel]:
	args = helper.get_first(program.parse_known_args())
	result = []

	for producer_name in args.producer:
		producer = load_producer(producer_name)
		producer.init(program)
		try:
			result.extend(producer.run())
		except IOError:
			sys.exit(wording.get('producer_crash').format(producer_name) + wording.get('exclamation_mark'))
	return result


def load_producer(producer_name : str) -> Any:
	try:
		return importlib.import_module('chroma_feedback.producer.' + producer_name)
	except ImportError:
		sys.exit(wording.get('producer_no').format(producer_name) + wording.get('exclamation_mark'))
