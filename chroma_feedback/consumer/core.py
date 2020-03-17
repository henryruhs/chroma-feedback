from typing import Any, Dict, List
from argparse import ArgumentParser
import importlib
from chroma_feedback import helper, wording


def process(program : ArgumentParser, status : str, *args, **kwargs) -> List[Dict[str, Any]]:
	program_args = helper.get_first(program.parse_known_args())
	result = []

	for consumer_name in program_args.consumer:
		consumer = load_consumer(consumer_name)
		consumer.init(program)
		result.extend(consumer.run(status, *args, **kwargs))
	return result


def load_consumer(consumer_name : str) -> Any:
	try:
		return importlib.import_module('chroma_feedback.consumer.' + consumer_name)
	except ImportError:
		exit(wording.get('consumer_no') + wording.get('exclamation_mark'))
