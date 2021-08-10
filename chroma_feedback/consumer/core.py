import sys
from typing import Any, List
from argparse import ArgumentParser
import importlib
from chroma_feedback import helper, wording
from chroma_feedback.typing import StatusType, ConsumerModel


def process(program : ArgumentParser, status : StatusType) -> List[ConsumerModel]:
	args = helper.get_first(program.parse_known_args())
	result = []

	for consumer_name in args.consumer:
		consumer = load_consumer(consumer_name)

		if consumer.support() is True:
			try:
				consumer.init(program)
				result.extend(consumer.run(status))
			except IOError:
				sys.exit(wording.get('consumer_crashed').format(consumer_name) + wording.get('exclamation_mark'))
		else:
			sys.exit(wording.get('consumer_not_supported').format(consumer_name) + wording.get('exclamation_mark'))
	return result


def load_consumer(consumer_name : str) -> Any:
	try:
		return importlib.import_module('chroma_feedback.consumer.' + consumer_name)
	except ImportError:
		sys.exit(wording.get('consumer_not_found').format(consumer_name) + wording.get('exclamation_mark'))
