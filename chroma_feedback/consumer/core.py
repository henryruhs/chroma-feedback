from typing import Any, Dict, List
from argparse import ArgumentParser
import importlib
from chroma_feedback import helper, wording


def process(program : ArgumentParser, status : str) -> List[Dict[str, Any]]:
	args = helper.get_first(program.parse_known_args())
	result = []

	for consumer_name in args.consumer:
		consumer = load_consumer(consumer_name)
		consumer.init(program)
		try:
			result.extend(consumer.run(status))
		except:
			exit(wording.get('consumer_crash').format(consumer_name) + wording.get('exclamation_mark'))
	return result


def load_consumer(consumer_name : str) -> Any:
	try:
		return importlib.import_module('chroma_feedback.consumer.' + consumer_name)
	except ImportError:
		exit(wording.get('consumer_no').format(consumer_name) + wording.get('exclamation_mark'))
