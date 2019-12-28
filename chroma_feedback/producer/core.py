from typing import Any, Dict, List
from argparse import ArgumentParser
import importlib
from chroma_feedback import helper, wording


def process(program : ArgumentParser) -> List[Dict[str, Any]]:
	args = helper.get_first(program.parse_known_args())
	result = []

	for producer_name in args.producer:
		producer = load_producer(producer_name)
		producer.init(program)
		result.extend(producer.run())
	return result


def load_producer(producer_name : str) -> Any:
	try:
		return importlib.import_module('chroma_feedback.producer.' + producer_name)
	except ImportError:
		exit(wording.get('producer_no') + wording.get('exclamation_mark'))
